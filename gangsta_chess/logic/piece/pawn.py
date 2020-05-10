from gangsta_chess.logic.piece.piece import *


class Pawn(Piece):
    def __init__(self, pos, team, Board):
        super().__init__(pos, team, Board)
        self.is_first_move = True
        self.relative_dir = 1 if self.team == 'w' else -1

    def find_valid_moves(self):
        super().find_valid_moves()
        if self.is_first_move:
            self._calculate_valid_moves([self.relative_dir, 0], 2)
        else:
            self._calculate_valid_moves([self.relative_dir, 0], 1)

        self._calculate_valid_moves([self.relative_dir, 1], 1, True)
        self._calculate_valid_moves([self.relative_dir, -1], 1, True)









