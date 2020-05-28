from socket import *
BUFFER = 1024


# localhost = 169.254.200.100
def connect(addr, port):
    s = socket()
    s.connect((addr, port))
    print(s.recv(BUFFER).decode('ascii'))
    s.send(b'client says hello')


def check_av_moves(piece):
    pass


def move(dst):
    pass
