from gangsta_chess.logic.piece.piece import *


class Pawn(Piece):
    def __init__(self, pos, team, Board):
        super().__init__(pos, team, Board)
        self.is_first_move = True

    def find_valid_moves(self):
        self.valid_moves = np.array([], dtype=int)
        if self.is_first_move:
            self.move_up_down(2, self.relative_dir)
        else:
            self.move_up_down(1, self.relative_dir)

        for i in range(len(self.valid_moves)):
            try:
                if self.board.board[tuple(self.valid_moves[i])].team == self.team:
                    self.valid_moves = np.delete(self.valid_moves, i)
            except AttributeError:
                continue






