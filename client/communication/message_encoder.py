import json


def to_json(message):
    return json.dumps(message, separators=(',', ':'))


def join_game(bot):
    return ['join', bot]


def check_moves(piece):
    return ['chk_sqrs', piece[0], piece[1]]


def move(sqr_from, sqr_to):
    return ['mv'] + sqr_from + sqr_to
