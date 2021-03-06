import json

from server.matchmaking.lobby import join


def decode(caller, msg):
    print(msg)
    msg = msg.decode('ascii')
    for line in msg.split():
        message = json.loads(line)
        if message[0] == 'chk_sqrs':
            caller.check_av_sqrs((message[1], message[2]))
        elif message[0] == 'mv':
            caller.move((message[1], message[2]))
        elif message[0] == 'join':
            join(caller, message[1])
        elif message[0] == 'promote':
            caller.promote(message[1])
