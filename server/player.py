class Player:
    def __init__(self):
        self.game = None

    def set_game(self, new_game):
        self.game = new_game

    def victory(self):
        pass

    def defeat(self):
        pass

    def draw(self):
        pass

    def your_turn(self):
        pass

    def opponent_turn(self):
        pass

    # piece - 'queen'/'bishop'/'rook'/'knight' when promoting a pawn,  None if otherwise
    def update_board(self, moves, piece):
        pass

    def send_av_moves(self, moves):
        pass

    def promote_pawn(self, x, y):
        pass
