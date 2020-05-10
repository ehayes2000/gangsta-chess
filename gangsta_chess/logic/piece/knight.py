from gangsta_chess.logic.piece.piece import *


class Knight(Piece):
    def __init__(self, pos, team, Board):
        super().__init__(pos, team, Board)

    def find_valid_moves(self):
        super().find_valid_moves()
        self._calculate_valid_moves([2, 1], 1)
        self._calculate_valid_moves([2, -1], 1)
        self._calculate_valid_moves([-2, 1], 1)
        self._calculate_valid_moves([-2, -1], 1)
        self._calculate_valid_moves([1, 2], 1)
        self._calculate_valid_moves([-1, 2], 1)
        self._calculate_valid_moves([1, -2], 1)
        self._calculate_valid_moves([-1, -2], 1)
