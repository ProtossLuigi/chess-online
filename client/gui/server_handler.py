from .queueWindow import QueueWindow

def game_start(color):
    print("game_start")
    queueWindow = QueueWindow()
    return queueWindow.game_start(color)

from .boardWidget import BoardWidget

def your_turn():
    pass  # TODO

def available_squares(squares):
    pass  # TODO

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


def opponent_turn():
    pass  # TODO


def promote_pawn(x, y):
    pass  # TODO


def update_board(moves, piece):
    pass  # TODO
