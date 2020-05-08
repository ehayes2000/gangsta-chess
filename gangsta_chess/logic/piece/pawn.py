from gangsta_chess.logic.piece.piece import *


class Pawn(Piece):
    def __init__(self, pos, type='pawn'):
        super().__init__(pos)
        self.type = type
        self.is_first_move = True
        self.is_queen = False

    # TODO implement capture

    def get_valid_moves(self):
        if self.is_first_move:
            self.is_first_move = False
            self.valid_moves = np.array([(self.pos[0], self.pos[1] + 1),
                                        (self.pos[0], self.pos[1] + 2)])
        else:
            self.valid_moves = np.array([(self.pos[0], self.pos[1] + 1)])


x = Pawn((0,1))
x.is_first_move = False
print(x.get_valid_moves())




