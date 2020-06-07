import threading

from . import message_encoder as me
from . import message_decoder as md
from ..player import Player
BUFFER = 1024


class ConnectedPlayer(Player, threading.Thread):
    def __init__(self, client_socket):
        threading.Thread.__init__(self)
        Player.__init__(self)
        self.socket = client_socket

    def run(self):
        while True:
            msg = self.socket.recv(BUFFER)
            if not msg:
                return
            md.decode(self, msg)

    def send(self, msg):
        json = me.to_json(msg)
        self.socket.send(json)

    def start_game(self, color):
        self.send(me.game_start(color))

    def victory(self):
        self.send(me.victory())

    def defeat(self):
        self.send(me.defeat())

    def draw(self):
        self.send(me.draw())

    def send_check(self):
        self.send(me.check())

    def your_turn(self):
        self.send(me.your_turn())

    def opponent_turn(self):
        self.send(me.opponent_turn())

    def update_board(self, moves, piece):
        self.send(me.update_board(moves, piece))

    def send_av_moves(self, moves):
        self.send(me.available_squares(moves))

    def promote_pawn(self, x, y):
        self.send(me.promote_pawn(x, y))

    def move(self, dst):
        self.game.move(self, dst)

    def check_av_sqrs(self, piece):
        self.game.check_available_moves(self, piece)

    def promote(self, name):
        self.game.promote(name)
