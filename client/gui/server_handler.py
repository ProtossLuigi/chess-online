from .globals import *

def game_start(color):
    print(color)
    gameWindowShow(color)

def your_turn():
    your_turn1()

def opponent_turn():
    opponent_turn1()

def available_squares(squares):
    windowGame.availableSquares()

def victory():
    pass  # TODO


def defeat():
    pass  # TODO


def draw():
    pass  # TODO


def opponent_dc():
    pass  # TODO


def check():
    pass  # TODO


def promote_pawn(x, y):
    pass  # TODO


def update_board(moves, piece):
    pass  # TODO
