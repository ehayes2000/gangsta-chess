from gangsta_chess.logic.piece.piece import *


class King(Piece):
    def __init__(self, team, Board):
        super().__init__(team, Board)
        self.in_check_mate = False

    def __str__(self):
        return '♔' if self.team == 'b' else '♚'

    # FIXME doesn't return true when it should
    def in_check(self):
        pos = tuple(np.array(self.pos()).flatten())
        for piece in self.board.pieces:
            if piece.team != self.team and pos in piece.valid_moves:
                return True
        return False

    def _remove_invalid_moves(self):
        for move in self.valid_moves:
            for piece in self.board.pieces:
                if piece.team != self.team and move in piece.valid_moves:
                    self.valid_moves.remove(move)

    def find_valid_moves(self):
        super()._find_valid_moves([[1, 0], [-1, 0], [0, 1], [0, -1],
                                   [1, 1], [1, -1], [-1, -1], [-1, 1]], 1)
        self._remove_invalid_moves()
        if len(self.valid_moves) == 0 and self.in_check():
            self.in_check_mate = True
