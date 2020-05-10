from gangsta_chess.logic.piece.piece import *


class Rook(Piece):
    def __init__(self, pos, team, Board):
        super().__init__(pos, team, Board)

    def find_valid_moves(self):
        super().find_valid_moves()
        self._calculate_valid_moves([1, 0])
        self._calculate_valid_moves([-1, 0])
        self._calculate_valid_moves([0, 1])
        self._calculate_valid_moves([0, -1])
