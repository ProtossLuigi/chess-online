from random import uniform

from server.player import Player


class DefaultBot(Player):
    def __init__(self):
        super().__init__()
        self.board = [[0 for _ in range(8)] for _ in range(8)]
        self.color = 0
        self.last_piece = None
        self.av_moves = []

    def get_av_moves(self, y, x):
        self.last_piece = (y, x)
        self.game.check_available_moves(self, self.last_piece)
        return self.av_moves

    def get_all_moves(self):
        moves = []
        for y in range(8):
            for x in range(8):
                if self.board[y][x] * self.color > 0:
                    moves += [((y, x), dst) for dst in self.get_av_moves(y, x)]
        return moves

    def update_board(self, moves, piece):
        if piece:
            move = moves[0]
            if piece == 'rook':
                self.board[move[1][0]][move[1][1]] = 2
            elif piece == 'bishop':
                self.board[move[1][0]][move[1][1]] = 3
            elif piece == 'knight':
                self.board[move[1][0]][move[1][1]] = 4
            elif piece == 'queen':
                self.board[move[1][0]][move[1][1]] = 5
            self.board[move[0][0]][move[0][1]] = 0
        else:
            for move in moves:
                self.board[move[1][0]][move[1][1]] = self.board[move[0][0]][move[0][1]]
                self.board[move[0][0]][move[0][1]] = 0

    def start_game(self, color):
        self.color = {'Bialy': 1, 'Czarny': -1}[color]
        self.board[0][0] = -2
        self.board[0][1] = -4
        self.board[0][2] = -3
        self.board[0][3] = -5
        self.board[0][4] = -6
        self.board[0][5] = -3
        self.board[0][6] = -4
        self.board[0][7] = -2
        for i in range(8):
            self.board[1][i] = -1
            self.board[6][i] = 1
        self.board[7][0] = 2
        self.board[7][1] = 4
        self.board[7][2] = 3
        self.board[7][3] = 5
        self.board[7][4] = 6
        self.board[7][5] = 3
        self.board[7][6] = 4
        self.board[7][7] = 2

    def your_turn(self):
        moves = self.get_all_moves()
        weights = []
        for move in moves:
            if self.board[move[1][0]][move[1][1]] * self.color < 0:
                weights.append(0.75)
            else:
                weights.append(0.25)
        cap = sum(weights)
        r = uniform(0., cap)
        s = 0.
        for i in range(len(moves)):
            if s <= r < s + weights[i]:
                if self.last_piece != (moves[i][0][1], moves[i]):
                    self.get_av_moves(moves[i][0][0], moves[i][0][1])
                self.game.move(self, moves[i][1])
                return
            s += weights[i]

    def send_av_moves(self, moves):
        self.av_moves = moves

    def promote_pawn(self, y, x):
        self.game.promote('queen')
