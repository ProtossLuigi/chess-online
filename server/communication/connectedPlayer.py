from ..player import Player
from socket import socket


class ConnectedPlayer(Player):
    def __init__(self):
        super().__init__()
        self.socket = None
        self.game = None

    def set_game(self, new_game):
        self.game = new_game

    def listen(self, player_socket):
        self.socket = player_socket
