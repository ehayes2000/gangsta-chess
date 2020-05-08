from gangsta_chess.logic.piece.piece import *


class Pawn(Piece):
    def __init__(self, pos):
        super().__init__(pos)
        self.is_first_move = True

    # TODO implement capture

    def get_valid_moves(self):
        if self.is_first_move:
            self.is_first_move = False
            self.valid_moves = np.array([(self.pos[0], self.pos[1] + 1),
                                        (self.pos[0], self.pos[1] + 2)])
        else:
            self.valid_moves = np.array([(self.pos[0], self.pos[1] + 1)])






