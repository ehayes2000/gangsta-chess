from gangsta_chess.logic.piece.piece import *


class Pawn(Piece):
    def __init__(self, team, Board):
        super().__init__(team, Board)
        self.is_first_move = True
        self.relative_dir = 1 if self.team == 'w' else -1

    def __str__(self):
        return '♙' if self.team == 'b' else '♟'

    def _find_pawn_moves(self):
        pos = np.array(self.pos()).flatten()
        step = [self.relative_dir, 0]
        if not self.is_first_move:
            if self._in_range(pos + step) and not self.board.board[tuple(pos + step)]:
                self.valid_moves.add(tuple(pos + step))
        else:
            for i in range(2):
                if self._in_range(pos + step) and not self.board.board[tuple(pos + step)]:
                    self.valid_moves.add(tuple(pos + step))
                    pos = pos + step
                else:
                    break
    def _find_pawn_captures(self):
        pos = np.array(self.pos()).flatten()
        steps = [[self.relative_dir, 1], [self.relative_dir, -1]]
        for step in steps:
            if self._in_range(pos + step) and self.board.board[tuple(pos + step)]:
                if self.board.board[tuple(pos + step)].team != self.team:
                    self.valid_moves.add(tuple(pos + step))

    def move(self, pos):
        if super().move(pos):
            self.is_first_move = False

    def find_valid_moves(self):
        self._find_pawn_moves()
        self._find_pawn_captures()







