import server.game_logic.chess_pieces as cp
from ..player import Player


class GamePlayer:
    def __init__(self):
        self.pieces = []
        self.opponent = None
        self.king = None

    def set_opponent(self, opponent):
        self.opponent = opponent


class Game:
    def __init__(self):
        self.board = [[]]

        self.white_player = GamePlayer()
        self.black_player = GamePlayer()

        self.board[0].append(cp.Rook(0, 0))
        self.board[0].append(cp.Knight(0, 1))
        self.board[0].append(cp.Bishop(0, 2))
        self.board[0].append(cp.Queen(0, 3))
        self.board[0].append(cp.King(0, 4))
        self.black_player.king = self.board[0][4]
        self.board[0].append(cp.Bishop(0, 5))
        self.board[0].append(cp.Knight(0, 6))
        self.board[0].append(cp.Rook(0, 7))

        self.board.append([])

        for i in range(8):
            self.board[1].append(cp.Pawn(1, i, 1))

        for i in range(2, 6):
            self.board.append([])
            for j in range(8):
                self.board[i].append(None)

        self.board.append([])

        for i in range(8):
            self.board[6].append(cp.Pawn(6, i, -1))

        self.board.append([])

        self.board[7].append(cp.Rook(7, 0))
        self.board[7].append(cp.Knight(7, 1))
        self.board[7].append(cp.Bishop(7, 2))
        self.board[7].append(cp.Queen(7, 3))
        self.board[7].append(cp.King(7, 4))
        self.white_player.king = self.board[7][4]
        self.board[7].append(cp.Bishop(7, 5))
        self.board[7].append(cp.Knight(7, 6))
        self.board[7].append(cp.Rook(7, 7))

        self.white_player.set_opponent(self.black_player)
        self.black_player.set_opponent(self.white_player)
        self.current_player = self.white_player

        self.black_player.pieces.append(self.board[0][4])
        for i in range(2):
            for j in range(8):
                if i == 0 and j == 4:
                    continue
                self.black_player.pieces.append(self.board[i][j])

        self.white_player.pieces.append(self.board[7][4])
        for i in range(6, 8):
            for j in range(8):
                if i == 7 and j == 4:
                    continue
                self.white_player.pieces.append(self.board[i][j])

    def set_field(self, x, y, piece):
        self.board[x][y] = piece
        if piece is not None:
            self.board[x][y].x = x
            self.board[x][y].y = y

    def is_check_after_move(self, x, y, dest_x, dest_y):
        temp = None
        if self.board[dest_x][dest_y] is not None:
            temp = self.board[dest_x][dest_y]
        self.set_field(dest_x, dest_y, self.board[x][y])
        self.set_field(x, y, None)
        result = self.is_check(self.current_player)
        self.set_field(x, y, self.board[dest_x][dest_y])
        if temp is not None:
            self.set_field(dest_x, dest_y, temp)
        else:
            self.set_field(dest_x, dest_y, None)

        return result

    def get_moves(self, x, y):
        moves = self.board[x][y].get_av_moves(self)
        updated_moves = []
        for move in moves:
            if not self.is_check_after_move(x, y, move[0], move[1]):
                updated_moves.append(move)
        return updated_moves

    def move_piece(self, x, y, dest_x, dest_y):
        if self.board[x][y] not in self.current_player.pieces:
            return
        if (dest_x, dest_y) not in self.get_moves(self, x, y):
            return
        if self.board[dest_x][dest_y] in self.current_player.opponent.pieces:
            self.current_player.opponent.pieces.remove(self.board[dest_x][dest_y])
        if isinstance(self.board[x][y], cp.Pawn):
            self.board[x][y].first_move = False
            if self.board[x][y].direction == -1 and dest_x == 0 or self.board[x][y].direction == 1 and dest_x == 7:
                self.set_field(dest_x, dest_y, self.board[x][y])
                self.set_field(x, y, None)
                return
        elif isinstance(self.board[x][y], cp.King):
            self.board[x][y].first_move = False
            if (y - dest_y) == 2:
                self.castling(self.current_player, 'left')
                return
            elif (y - dest_y) == -2:
                self.castling(self.current_player, 'right')
                return
        elif isinstance(self.board[x][y], cp.Rook):
            self.board[x][y].first_move = False
        self.set_field(dest_x, dest_y, self.board[x][y])
        self.set_field(x, y, None)
        self.change_player()

    def castling(self, player, direction):
        x = player.king.x
        if direction == 'right':
            self.set_field(x, 6, player.king)
            self.set_field(x, 4, None)
            self.set_field(x, 5, self.board[x][7])
            self.set_field(x, 7, None)
        elif direction == 'left':
            self.set_field(x, 2, player.king)
            self.set_field(x, 4, None)
            self.set_field(x, 3, self.board[x][0])
            self.set_field(x, 0, None)
        self.change_player()

    def change_player(self):
        self.current_player = self.current_player.opponent

    def promote_pawn(self, x, y, piece_name):
        self.current_player.pieces.remove(self.board[x][y])
        self.set_field(x, y, None)
        if piece_name == 'knight':
            knight = cp.Knight(x, y)
            self.set_field(x, y, knight)
            self.current_player.pieces.append(knight)
        elif piece_name == 'rook':
            rook = cp.Rook(x, y)
            self.set_field(x, y, rook)
            self.current_player.pieces.append(rook)
        elif piece_name == 'bishop':
            bishop = cp.Bishop(x, y)
            self.set_field(x, y, bishop)
            self.current_player.pieces.append(bishop)
        elif piece_name == 'queen':
            queen = cp.Queen(x, y)
            self.set_field(x, y, queen)
            self.current_player.pieces.append(queen)

        self.change_player()

    def pass_move(self):
        self.change_player()

    def is_check(self, player):
        x = player.king.x
        y = player.king.y
        for piece in player.opponent.pieces:
            if (x, y) in piece.get_av_moves(self):
                return True
        return False

    def is_checkmate(self, player):
        for piece in player.pieces:
            moves = self.get_moves(piece.x, piece.y)
            if moves:
                return False
        return True

    def is_draw(self):
        if not self.is_check(self.current_player):
            moves = []
            for piece in self.current_player.pieces:
                moves += self.get_moves(piece.x, piece.y)
            if not moves:
                return True
        else:
            if len(self.current_player.pieces) == 1 and len(self.current_player.opponent.pieces) == 1:
                return True
            elif len(self.current_player.pieces) == 1 and len(self.current_player.opponent.pieces) == 2:
                if isinstance(self.current_player.opponent.pieces[1], cp.Bishop) or \
                        isinstance(self.current_player.opponent.pieces[1], cp.Knight):
                    return True
            elif len(self.current_player.pieces) == 2 and len(self.current_player.opponent.pieces) == 2:
                if isinstance(self.current_player.pieces[1], cp.Bishop) and \
                        isinstance(self.current_player.opponent.pieces[1], cp.Bishop):
                    x_p = self.current_player.pieces[1].x
                    y_p = self.current_player.pieces[1].y
                    x_o = self.current_player.opponent.pieces[1].x
                    y_o = self.current_player.opponent.pieces[1].y
                    if (8 % (x_p + y_p) == 0 and 8 % (x_o + y_o) == 0) or (
                            8 % (x_p + y_p) == 1 and 8 % (x_o + y_o) == 1):
                        return True
        return False


def get_new_game():
    return Game()
