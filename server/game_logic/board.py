import server.game_logic.chess_pieces as cp


class Player:
    def __init__(self):
        self.pieces = []
        self.opponent = None

    def set_opponent(self, opponent):
        self.opponent = opponent

    def add_piece(self, piece):
        self.pieces.append(piece)


class Game:
    def __init__(self):
        self.board = [[]]

        self.board[0].append(cp.Rook(0, 0))
        self.board[0].append(cp.Knight(0, 1))
        self.board[0].append(cp.Bishop(0, 2))
        self.board[0].append(cp.Queen(0, 3))
        self.board[0].append(cp.King(0, 4))
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
        self.board[7].append(cp.Bishop(7, 5))
        self.board[7].append(cp.Knight(7, 6))
        self.board[7].append(cp.Rook(7, 7))

        self.white_player = Player()
        self.black_player = Player()
        self.white_player.set_opponent(self.black_player)
        self.black_player.set_opponent(self.white_player)
        self.current_player = self.white_player

        for i in range(2):
            for j in range(8):
                self.black_player.add_piece(self.board[i][j])

        for i in range(6, 8):
            for j in range(8):
                self.white_player.add_piece(self.board[i][j])

    def set_field(self, x, y, piece):
        self.board[x][y] = piece
        if piece is not None:
            self.board[x][y].x = x
            self.board[x][y].y = y

    def move_piece(self, x, y, dest_x, dest_y):
        if self.board[x][y] not in self.current_player.pieces:
            print("That is not current player's piece!")
            return
        if (dest_x, dest_y) not in self.board[x][y].get_av_moves(self):
            print("That moves is not available!")
            return
        if self.board[dest_x][dest_y] in self.current_player.opponent.pieces:
            self.current_player.opponent.pieces.remove(self.board[dest_x][dest_y])
        self.set_field(dest_x, dest_y, self.board[x][y])
        self.set_field(x, y, None)
        self.change_player()

    def change_player(self):
        self.current_player = self.current_player.opponent

    def print_board(self):
        print(' ', end=' ')
        for i in range(8):
            print(i, end=' ')
        for i in range(8):
            print()
            print(i, end=' ')
            for j in range(8):
                if isinstance(self.board[i][j], cp.Pawn) and self.board[i][j] in self.black_player.pieces:
                    print('P', end=' ')
                elif isinstance(self.board[i][j], cp.Pawn) and self.board[i][j] in self.white_player.pieces:
                    print('p', end=' ')
                elif isinstance(self.board[i][j], cp.Rook) and self.board[i][j] in self.black_player.pieces:
                    print('W', end=' ')
                elif isinstance(self.board[i][j], cp.Rook) and self.board[i][j] in self.white_player.pieces:
                    print('w', end=' ')
                elif isinstance(self.board[i][j], cp.Knight) and self.board[i][j] in self.black_player.pieces:
                    print('R', end=' ')
                elif isinstance(self.board[i][j], cp.Knight) and self.board[i][j] in self.white_player.pieces:
                    print('r', end=' ')
                elif isinstance(self.board[i][j], cp.Bishop) and self.board[i][j] in self.black_player.pieces:
                    print('B', end=' ')
                elif isinstance(self.board[i][j], cp.Bishop) and self.board[i][j] in self.white_player.pieces:
                    print('b', end=' ')
                elif isinstance(self.board[i][j], cp.Queen) and self.board[i][j] in self.black_player.pieces:
                    print('Q', end=' ')
                elif isinstance(self.board[i][j], cp.Queen) and self.board[i][j] in self.white_player.pieces:
                    print('q', end=' ')
                elif isinstance(self.board[i][j], cp.King) and self.board[i][j] in self.black_player.pieces:
                    print('K', end=' ')
                elif isinstance(self.board[i][j], cp.King) and self.board[i][j] in self.white_player.pieces:
                    print('k', end=' ')
                else:
                    print(' ', end=' ')


def get_new_game():
    return Game()


"""g = Game()
g.print_board()
print()
print()

while g.board[0][4] in g.black_player.pieces and g.board[7][4] in g.white_player.pieces:
    if g.current_player is g.white_player:
        print("Current turn - white player")
    else:
        print("Current turn - black player")
    x = input()
    y = input()
    print(g.board[int(x)][int(y)].get_av_moves(g))
    z = input()
    t = input()
    g.move_piece(int(x), int(y), int(z), int(t))
    g.print_board()
    print()
    print()"""
