

def game_start(color):
    from .globals import gameWindowShow
    print(color)
    gameWindowShow(color)

def your_turn():
    from .globals import your_turn1
    your_turn1()

def opponent_turn():
    from .globals import opponent_turn1
    opponent_turn1()

def available_squares(squares):
    print(squares)

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
