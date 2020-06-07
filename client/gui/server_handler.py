
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
    print(squares)
    from .globals import available_squares1
    available_squares1(squares)

def update_board(moves, piece):
    from .globals import update_board1
    update_board1(moves, piece)

def victory():
    from .globals import victory1
    victory1()

def defeat():
    from .globals import defeat1
    defeat1()

def draw():
    from .globals import draw1
    draw1()

def opponent_dc():
    pass  # TODO

def check():
    from .globals import check1
    check1()

def promote_pawn(x, y):
    from .globals import promote_pawn1
    promote_pawn1(x, y)