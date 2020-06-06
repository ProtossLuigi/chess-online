import json


def to_json(msgs):
    return bytearray(json.dumps(msgs, separators=(',', ':')) + '\n', encoding='ascii')


def available_squares(squares):
    return ['av_sqrs'] + squares


def game_start(color):
    return ['start', color]


def victory():
    return ['victory']


def defeat():
    return ['defeat']


def draw():
    return ['draw']


def opponent_dc():
    return ['disconnect']


def check():
    return ['check']


def your_turn():
    return ['turn', True]


def opponent_turn():
    return ['turn', False]


def promote_pawn(x, y):
    return ['promote', x, y]


def update_board(moves, piece):
    return ['update', moves, piece]
