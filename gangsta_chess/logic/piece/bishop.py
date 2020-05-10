from gangsta_chess.logic.piece.piece import *


class Bishop(Piece):
    def __init__(self, pos, team, Board):
        super().__init__(pos, team, Board)

    def find_valid_moves(self):
        super().find_valid_moves()
        self._calculate_valid_moves([1, 1])
        self._calculate_valid_moves([-1, -1])
        self._calculate_valid_moves([1, -1])
        self._calculate_valid_moves([-1, 1])

