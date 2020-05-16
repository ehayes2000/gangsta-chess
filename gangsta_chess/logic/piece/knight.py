from gangsta_chess.logic.piece.piece import *


class Knight(Piece):
    def __init__(self, team, Board):
        super().__init__(team, Board)

    def __str__(self):
        return '♘' if self.team == 'b' else '♞'

    def find_valid_moves(self):
        pos = self.pos()
        super()._find_valid_moves([[2, 1], [2, -1], [-2, 1], [-2, -1],
                                   [1, 2], [1, -2], [-1, 2], [-1, -2]], 1)


