from gangsta_chess.logic.piece.piece import *


class King(Piece):
    def __init__(self, team):
        super().__init__(team, np.array([[1, 0], [-1, 0], [0, 1], [0, -1],
                                         [1, 1], [1, -1], [-1, -1], [-1, 1]]))
        self.in_check_mate = False
        self.line_of_sight = {}  # {piece:dir}
        self.line_of_sight_updated = False
        self.in_check = False

    def __str__(self):
        return '♔' if self.team == 'b' else '♚'

    # Remove moves that would put the king into a valid move for an opposing piece
    def _remove_invalid_moves(self, board):
        for move in self.theoretical_moves:
            for piece in board.pieces:
                if piece.team != self.team and move in piece.theoretical_moves:
                    self.theoretical_moves.remove(move)

    def calculate_actual_moves(self, is_in_check):
        super().calculate_actual_moves(is_in_check)
        one_away_moves = []
        for move in self.actual_moves:
            if abs(move[0] - self.pos[0]) > 1 or abs(move[1] - self.pos[1]) > 1:
                continue
            one_away_moves.append(move)
        self.actual_moves = one_away_moves

    def find_valid_moves(self, board):
        super()._find_valid_moves(self.move_template, 1, board)

        def get_line_of_sight(self):
            if not self.line_of_sight_updated:
                self._update_line_of_sight()
            return self.line_of_sight

        def in_check(self, board):
            # loop though every piece on the board
            for piece in board.pieces:
                # if the piece is on the other team check if it can move to where the king is
                if piece.team != self.team:
                    # if the piece can move to where the king is, the king is in check so return True
                    if self.pos in piece.theoretical_moves:
                        return True
            return False

        # self._remove_invalid_moves(board)
        # if len(self.valid_moves) == 0 and self.in_check(board):
        #     self.in_check_mate = True
