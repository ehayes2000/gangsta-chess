from gangsta_chess.logic.piece.piece import *


class King(Piece):
    def __init__(self, team, pos):
        super().__init__(team, pos)
        self.in_check_mate = False

    def __str__(self):
        return '♔' if self.team == 'b' else '♚'

    def in_check(self, board):
        # loop though every piece on the board
        for piece in board.pieces:
            # if the piece is on the other team check if it can move to where the king is
            if piece.team != self.team:
                # if the piece can move to where the king is, the king is in check so return True
                if self.pos in piece.valid_moves:
                    return True
        return False

    # Remove moves that would put the king into a valid move for an opposing piece
    def _remove_invalid_moves(self, board):
        for move in self.valid_moves:
            for piece in board.pieces:
                if piece.team != self.team and move in piece.valid_moves:
                    self.valid_moves.remove(move)

    def find_valid_moves(self, board):
        super()._find_valid_moves([[1, 0], [-1, 0], [0, 1], [0, -1],
                                   [1, 1], [1, -1], [-1, -1], [-1, 1]], 1, board)

        # self._remove_invalid_moves(board)
        # if len(self.valid_moves) == 0 and self.in_check(board):
        #     self.in_check_mate = True
