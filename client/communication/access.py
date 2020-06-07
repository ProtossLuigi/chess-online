from socket import socket, error

from . import message_encoder as me
from client.communication.connection import send
from client.communication.message_decoder import decode

BUFFER = 1024
active_socket = None


# localhost = 169.254.200.100
def connect(addr, port):
    global active_socket
    active_socket = socket()
    active_socket.connect((addr, port))


def listen():
    while True:
        msg = active_socket.recv(BUFFER)
        print(msg)
        if not msg:
            raise error
        decode(msg)


def join(bot):
    send(active_socket, me.join_game(bot))


def check_av_moves(piece):
    send(active_socket, me.check_moves(piece))


def move(dst):
    send(active_socket, me.move(dst))

