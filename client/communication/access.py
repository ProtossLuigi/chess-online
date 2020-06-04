from socket import socket, error

from client.communication.message_decoder import decode

BUFFER = 1024


# localhost = 169.254.200.100
def connect(addr, port):
    s = socket()
    s.connect((addr, port))
    return s


def listen(socket_):
    while True:
        msg = socket_.recv(BUFFER)
        if not msg:
            raise error
        decode(msg)


def join(bot):
    pass


def check_av_moves(piece):
    pass


def move(dst):
    pass
