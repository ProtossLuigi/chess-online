from ..player import Player
from socket import socket


class ConnectedPlayer(Player):
    def __init__(self):
        super().__init__()
        self.socket = None

    def listen(self):
        pass
