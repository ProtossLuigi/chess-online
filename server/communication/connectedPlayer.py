import threading

from .listen import BUFFER
from .message_decoder import decode
from .message_encoder import to_json
from ..player import Player


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
            decode(self, msg)

    def send(self, msg):
        json = to_json(msg)
        self.socket.send(json)
