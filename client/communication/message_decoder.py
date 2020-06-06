import json

from ..gui.server_handler import *


def decode(message):
    message = json.loads(message.decode('ascii'))
    if message[0] == 'av_sqrs':
        available_squares(message[1:])
    elif message[0] == 'start':
        game_start(message[1])
    elif message[0] == 'victory':
        victory()
    elif message[0] == 'defeat':
        defeat()
    elif message[0] == 'draw':
        draw()
    elif message[0] == 'disconnect':
        opponent_dc()
    elif message[0] == 'check':
        check()
    elif message[0] == 'turn':
        if message[1]:
            your_turn()
        else:
            opponent_turn()
    elif message[0] == 'update':
        update_board(message[1], message[2])
    elif message[0] == 'promote':
        promote_pawn(message[1], message[2])
