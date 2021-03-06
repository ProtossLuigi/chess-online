from abc import ABC


class ChessPiece(ABC):
    def get_av_moves(self, game):
        pass


class Pawn(ChessPiece):
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction
        self.first_move = True

    def get_av_moves(self, game):
        x = self.x
        y = self.y
        moves = []
        if game.board[x][y] in game.current_player.pieces:
            player = game.current_player
        else:
            player = game.current_player.opponent

        if game.board[x + self.direction][y] is None:
            moves.append((x + self.direction, y))
            if self.first_move:
                if game.board[x + 2 * self.direction][y] is None:
                    moves.append((x + 2 * self.direction, y))
        if y > 0:
            if game.board[x + self.direction][y - 1] in player.opponent.pieces:
                moves.append((x + self.direction, y - 1))
        if y < 7:
            if game.board[x + self.direction][y + 1] in player.opponent.pieces:
                moves.append((x + self.direction, y + 1))

        return moves


class Knight(ChessPiece):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_av_moves(self, game):
        x = self.x
        y = self.y
        moves = []
        if game.board[x][y] in game.current_player.pieces:
            player = game.current_player
        else:
            player = game.current_player.opponent

        if x - 2 >= 0 and y - 1 >= 0:
            if game.board[x - 2][y - 1] not in player.pieces:
                moves.append((x - 2, y - 1))
        if x - 2 >= 0 and y + 1 < 8:
            if game.board[x - 2][y + 1] not in player.pieces:
                moves.append((x - 2, y + 1))
        if x - 1 >= 0 and y - 2 >= 0:
            if game.board[x - 1][y - 2] not in player.pieces:
                moves.append((x - 1, y - 2))
        if x + 1 < 8 and y - 2 >= 0:
            if game.board[x + 1][y - 2] not in player.pieces:
                moves.append((x + 1, y - 2))
        if x - 1 >= 0 and y + 2 < 8:
            if game.board[x - 1][y + 2] not in player.pieces:
                moves.append((x - 1, y + 2))
        if x + 1 < 8 and y + 2 < 8:
            if game.board[x + 1][y + 2] not in player.pieces:
                moves.append((x + 1, y + 2))
        if x + 2 < 8 and y - 1 >= 0:
            if game.board[x + 2][y - 1] not in player.pieces:
                moves.append((x + 2, y - 1))
        if x + 2 < 8 and y + 1 < 8:
            if game.board[x + 2][y + 1] not in player.pieces:
                moves.append((x + 2, y + 1))

        return moves


class Bishop(ChessPiece):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_av_moves(self, game):
        x = self.x
        y = self.y
        moves = []
        if game.board[x][y] in game.current_player.pieces:
            player = game.current_player
        else:
            player = game.current_player.opponent

        i = 1
        while x - i >= 0 and y - i >= 0:
            if game.board[x - i][y - i] in player.pieces:
                break
            elif game.board[x - i][y - i] is None:
                moves.append((x - i, y - i))
            else:
                moves.append((x - i, y - i))
                break
            i += 1

        i = 1
        while x + i < 8 and y - i >= 0:
            if game.board[x + i][y - i] in player.pieces:
                break
            elif game.board[x + i][y - i] is None:
                moves.append((x + i, y - i))
            else:
                moves.append((x + i, y - i))
                break
            i += 1

        i = 1
        while x + i < 8 and y + i < 8:
            if game.board[x + i][y + i] in player.pieces:
                break
            elif game.board[x + i][y + i] is None:
                moves.append((x + i, y + i))
            else:
                moves.append((x + i, y + i))
                break
            i += 1

        i = 1
        while x - i >= 0 and y + i < 8:
            if game.board[x - i][y + i] in player.pieces:
                break
            elif game.board[x - i][y + i] is None:
                moves.append((x - i, y + i))
            else:
                moves.append((x - i, y + i))
                break
            i += 1

        return moves


class Rook(ChessPiece):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.first_move = True

    def get_av_moves(self, game):
        x = self.x
        y = self.y
        moves = []
        if game.board[x][y] in game.current_player.pieces:
            player = game.current_player
        else:
            player = game.current_player.opponent

        i = 1
        while x + i < 8:
            if game.board[x + i][y] in player.pieces:
                break
            elif game.board[x + i][y] is None:
                moves.append((x + i, y))
            else:
                moves.append((x + i, y))
                break
            i += 1

        i = 1
        while x - i >= 0:
            if game.board[x - i][y] in player.pieces:
                break
            elif game.board[x - i][y] is None:
                moves.append((x - i, y))
            else:
                moves.append((x - i, y))
                break
            i += 1

        i = 1
        while y - i >= 0:
            if game.board[x][y - i] in player.pieces:
                break
            elif game.board[x][y - i] is None:
                moves.append((x, y - i))
            else:
                moves.append((x, y - i))
                break
            i += 1

        i = 1
        while y + i < 8:
            if game.board[x][y + i] in player.pieces:
                break
            elif game.board[x][y + i] is None:
                moves.append((x, y + i))
            else:
                moves.append((x, y + i))
                break
            i += 1

        return moves


class Queen(ChessPiece):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_av_moves(self, game):
        x = self.x
        y = self.y
        temp_bishop = Bishop(x, y)
        temp_rook = Rook(x, y)
        b_moves = temp_bishop.get_av_moves(game)
        r_moves = temp_rook.get_av_moves(game)
        del temp_bishop
        del temp_rook
        moves = b_moves + r_moves
        return moves


class King(ChessPiece):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.first_move = True

    def get_av_moves(self, game):
        x = self.x
        y = self.y
        moves = []
        if game.board[x][y] in game.current_player.pieces:
            player = game.current_player
        else:
            player = game.current_player.opponent

        if x - 1 >= 0 and y - 1 >= 0:
            if game.board[x - 1][y - 1] not in player.pieces:
                moves.append((x - 1, y - 1))
        if x - 1 >= 0:
            if game.board[x - 1][y] not in player.pieces:
                moves.append((x - 1, y))
        if x - 1 >= 0 and y + 1 < 8:
            if game.board[x - 1][y + 1] not in player.pieces:
                moves.append((x - 1, y + 1))
        if y + 1 < 8:
            if game.board[x][y + 1] not in player.pieces:
                moves.append((x, y + 1))
        if x + 1 < 8 and y + 1 < 8:
            if game.board[x + 1][y + 1] not in player.pieces:
                moves.append((x + 1, y + 1))
        if x + 1 < 8:
            if game.board[x + 1][y] not in player.pieces:
                moves.append((x + 1, y))
        if x + 1 < 8 and y - 1 >= 0:
            if game.board[x + 1][y - 1] not in player.pieces:
                moves.append((x + 1, y - 1))
        if y - 1 >= 0:
            if game.board[x][y - 1] not in player.pieces:
                moves.append((x, y - 1))

        if self.first_move and player is game.current_player:
            if not game.is_check(player):
                if isinstance(game.board[x][7], Rook) and game.board[x][7] in player.pieces and game.board[x][7].first_move:
                    if game.board[x][5] is None and game.board[x][6] is None:
                        moves.append((x, y + 2))
                if isinstance(game.board[x][0], Rook) and game.board[x][0] in player.pieces and game.board[x][0].first_move:
                    if game.board[x][3] is None and game.board[x][2] is None and game.board[x][1] is None:
                        moves.append((x, y - 2))
        return moves
