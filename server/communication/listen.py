from socket import *
from server.communication.connectedPlayer import ConnectedPlayer

BUFFER = 1024


def listen():
    server_socket = socket()
    server_socket.bind((gethostname(), 0))
    server_socket.listen(5)
    print('server running on', server_socket.getsockname())
    while True:
        client, addr = server_socket.accept()
        new_player = ConnectedPlayer(client)
        new_player.start()
        print('got a player')
