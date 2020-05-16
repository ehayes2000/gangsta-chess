from gangsta_chess.logic.piece.piece import *


class Queen(Piece):
    def __init__(self, team, Board):
        super().__init__(team, Board)

    def __str__(self):
        return '♕' if self.team == 'b' else '♛'

    def find_valid_moves(self):
        super()._find_valid_moves([[1, 0], [-1, 0], [0, 1], [0, -1],
                                   [1, 1], [-1, 1], [1, -1], [-1, -1]], 10)


