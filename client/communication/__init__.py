from socket import *
BUFFER = 1024


# localhost = 169.254.200.100
addr = input('enter server address ')
port = eval(input('enter port number '))
s = socket()
s.connect((addr, port))
print(s.recv(BUFFER).decode('ascii'))
s.send(b'client says hello')
