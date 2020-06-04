import json


def to_json(msgs):
    return bytearray(json.dumps(msgs, separators=(',', ':')), encoding='ascii')


def available_squares(squares):
    return ['av_sqrs'] + squares


def moves(mvs):
    return ['moves', mvs]


def game_start(color):
    return ['start', color]


def victory():
    return ['victory']


def defeat():
    return ['defeat']


def opponent_dc():
    return ['disconnect']
