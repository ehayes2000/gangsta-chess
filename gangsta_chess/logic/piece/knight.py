from gangsta_chess.logic.piece.piece import *


class Knight(Piece):
    def __str__(self):
        return '♘' if self.team == 'b' else '♞'

    def find_valid_moves(self, board):
        pos = self.pos()
        super()._find_valid_moves([[2, 1], [2, -1], [-2, 1], [-2, -1],
                                   [1, 2], [1, -2], [-1, 2], [-1, -2]], 1, board)


