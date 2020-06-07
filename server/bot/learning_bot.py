from random import random

from server.bot.model import ResidualCNN
from server.player import Player
import numpy as np

# pawn = 1
# rook = 2
# bishop = 3
# knight = 4
# queen = 5
# king = 6


def coords_to_index(t):
    return 8 * t[1] + t[0]


def index_to_coords(i):
    return i % 8, i // 8


class TrainedBot(Player):
    def __init__(self):
        super().__init__()
        self.board = np.array([[0 for _ in range(65)] + [1]])
        self.color = 0
        self.last_piece = None
        self.av_moves = []
        self.nn = ResidualCNN((1, 66), (64, 64))
        try:
            saved_model = self.nn.read()
            self.nn.model.set_weights(saved_model.get_weights())
        except FileNotFoundError:
            pass

    def filter_moves(self, moves):
        move_weights = []
        for i in range(64):
            if self.board[0][i] * self.color > 0:
                x_from, y_from = index_to_coords(i)
                for move in self.get_av_moves(x_from, y_from):
                    move_weights.append([(x_from, y_from), move, moves[i][coords_to_index(move)]])
        return move_weights

    def get_av_moves(self, x, y):
        self.last_piece = (x, y)
        self.game.check_available_moves(self, self.last_piece)
        return self.av_moves

    def update_board(self, moves, piece):
        if piece:
            if piece == 'rook':
                self.board[0][coords_to_index(moves[0][1])] = 2
            elif piece == 'bishop':
                self.board[0][coords_to_index(moves[0][1])] = 3
            elif piece == 'knight':
                self.board[0][coords_to_index(moves[0][1])] = 4
            elif piece == 'queen':
                self.board[0][coords_to_index(moves[0][1])] = 5
            self.board[0][coords_to_index(moves[0][0])] = 0
        else:
            for move in moves:
                self.board[0][coords_to_index(move[1])] = self.board[0][coords_to_index(move[0])]
                self.board[0][coords_to_index(move[0])] = 0

    def start_game(self, color):
        self.color = {'white': 1, 'black': -1}[color]
        self.board[0][65] = self.color
        self.board[0][0] = -2
        self.board[0][1] = -4
        self.board[0][2] = -3
        self.board[0][3] = -5
        self.board[0][4] = -6
        self.board[0][5] = -3
        self.board[0][6] = -4
        self.board[0][7] = -2
        for i in range(8, 16):
            self.board[0][i] = -1
        for i in range(48, 56):
            self.board[0][i] = 1
        self.board[0][56] = 2
        self.board[0][57] = 4
        self.board[0][58] = 3
        self.board[0][59] = 5
        self.board[0][60] = 6
        self.board[0][61] = 3
        self.board[0][62] = 4
        self.board[0][63] = 2

    def your_turn(self):
        model_input = self.nn.convertToModelInput(self.board)
        preds = self.nn.model.predict(model_input)
        moves = self.filter_moves(preds)
        cap = sum(move[2] for move in moves)
        r = random.uniform(0., cap)
        s = 0.
        for i in range(len(moves)):
            if s <= r < s + moves[i][2]:
                if not self.last_piece == moves[i][0]:
                    self.get_av_moves(moves[i][0][0], moves[i][0][1])
                self.game.move(self, moves[i][1])
                return
            else:
                s += moves[i][2]
        raise RuntimeError

    def send_av_moves(self, moves):
        self.av_moves = moves

    def promote_pawn(self, x, y):
        self.game.promote('queen')
