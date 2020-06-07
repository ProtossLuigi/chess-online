
def queue_start():
    from .globals import queueWindowShow
    queueWindowShow()

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
    from .globals import available_squares1
    available_squares1(squares)

def update_board(moves, piece):
    from .globals import update_board1
    update_board1(moves, piece)

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
    from .globals import promote_pawn1
    promote_pawn1(x, y)