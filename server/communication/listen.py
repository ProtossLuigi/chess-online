from socket import *
BUFFER = 1024


def listen():
    server_socket = socket()
    server_socket.bind((gethostname(), 0))
    server_socket.listen(5)
    print('server running on', server_socket.getsockname())
    while True:
        client, addr = server_socket.accept()
        client.send(b'server says hello')
        print(client.recv(BUFFER).decode('ascii'))
        client.close()
