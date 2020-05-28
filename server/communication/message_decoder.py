import json


def decode(rec_player, message):
    message = json.loads(message)
    if message[0] == 'chk_sqrs':
        pass
    elif message[0] == 'mv':
        pass
    elif message[0] == 'join':
        pass
