from gangsta_chess.logic.piece.piece import *


class Bishop(Piece):
    def __init__(self, team, Board):
        super().__init__(team, Board)

    def __str__(self):
        return '♗' if self.team == 'b' else '♝'


    def find_valid_moves(self):
        super()._find_valid_moves([[1, 1], [1, -1], [-1, 1], [-1, -1]], 10)
