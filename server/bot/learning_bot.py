from server.player import Player
import numpy as np

# pawn = 1
# rook = 2
# bishop = 3
# knight = 4
# queen = 5
# king = 6


class LearningBot(Player):
    def __init__(self):
        super().__init__()
        self.board = np.array([0 for _ in range(64)])

    def update_board(self, moves, piece):
        if piece:
            if piece == 'rook':
                self.board[moves[0][1]] = 2
            elif piece == 'bishop':
                self.board[moves[0][1]] = 3
            elif piece == 'knight':
                self.board[moves[0][1]] = 4
            elif piece == 'queen':
                self.board[moves[0][1]] = 5
            self.board[moves[0][0]] = 0
        else:
            for move in moves:
                self.board[move[1]] = self.board[move[0]]
                self.board[move[0]] = 0
