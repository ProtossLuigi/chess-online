import json

from server.matchmaking.lobby import join


def decode(caller, message):
    message = json.loads(message.decode('ascii'))
    if message[0] == 'chk_sqrs':
        caller.check_av_sqrs((message[1], message[2]))
    elif message[0] == 'mv':
        caller.move((message[1], message[2]))
    elif message[0] == 'join':
        join(caller, message[1])
