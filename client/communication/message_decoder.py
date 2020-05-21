import json


def decode(message):
    message = json.loads(message)
    if message[0] == 'av_sqrs':
        pass
    elif message[0] == 'moves':
        pass
    elif message[0] == 'start':
        pass
    elif message[0] == 'victory':
        pass
    elif message[0] == 'defeat':
        pass
    elif message[0] == 'disconnect':
        pass
