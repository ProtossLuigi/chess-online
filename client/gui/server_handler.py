from .queueWindow import QueueWindow

def game_start(color):
    print("game_start")
    queueWindow = QueueWindow()
    return queueWindow.game_start(color)

from .boardWidget import BoardWidget
boardWidget = BoardWidget()

def your_turn():
    boardWidget.your_turn()

def opponent_turn():
    boardWidget.opponent_turn()

def available_squares(squares):
    boardWidget.available_squares(squares)

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
