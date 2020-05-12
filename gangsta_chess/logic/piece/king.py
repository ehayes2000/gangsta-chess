from gangsta_chess.logic.piece.piece import *


class King(Piece):
    def __init__(self, pos, team, Board):
        super().__init__(pos, team, Board)
        self.in_check = False
        self.in_check_mate = False

    def _find_valid_moves(self):
        super()._find_valid_moves()
        self._calculate_valid_moves([1, 0], 1)
        self._calculate_valid_moves([-1, 0], 1)
        self._calculate_valid_moves([0, 1], 1)
        self._calculate_valid_moves([0, -1], 1)
        self._calculate_valid_moves([1, 1], 1)
        self._calculate_valid_moves([1, -1], 1)
        self._calculate_valid_moves([-1, 1], 1)
        self._calculate_valid_moves([-1, -1], 1)
        # TODO check for 'check/check-mate'
        remaining_moves_ = None
        for i in range(len(self.valid_moves)):

            # for j in self.board.board[tuple(self.valid_moves[i])].can_move_here:
            #     if j.team != self.team:
            #         self.valid_moves = np.delete(self.valid_moves, i)
            #         break
            if any(j.team != self.team for j in self.board.board[tuple(self.valid_moves[i])].can_move_here):
                self.valid_moves = np.delete(self.valid_moves, i)
                break

        #
        # if all(tuple(i) != self.pos for i in self.valid_moves):
        #     self.in_check = True
        #
        # if len(self.valid_moves) == 0:
        #     self.in_check_mate = True

        super()._update_tiles(True)

    def in_check(self):
        pass


