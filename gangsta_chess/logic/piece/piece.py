import numpy as np


class Piece:

    # *THEORETICAL MOVES* (make no physical changes)
    # 0. Use valid_moves to find list of possible moves
    # 1. will the move unblock another piece and allow it to check the king O(1) + O(4)
    #   O(1) lookup time for blocking dictionary
    #   Only need to check for enemies checking king
    #   *Prevents pieces from moving a piece out of the way so that the king is in check*
    # 2. will the move block another piece that was previously checking the kingO(16 * 4 * 4)
    #   16 - pieces, 4 - avg directions, 4 - avg moves
    #   Only needed when king is in check
    #   *Ensures that if the king is in check the next move unchecks the king
    # Now we have valid moves

    # *PIECE IS MOVED* (make physical changes)
    # 1. when a pieces is moved, it no longer blocks some pieces O(1) + O(avg moves)
    #   update those pieces moves
    # 2. when a pieces is moved, it may block new pieces
    #   update those pieces moves

    # Initialize piece with team and position
    def __init__(self, team, move_template):
        # INSTANCE
        self.team = team

        self.pos = None
        self.is_captured = False
        self.valid_moves = {}               # {dir : [moves]} theoretical
        self.move_template = move_template
        self.actual_moves = []

        # FLAGS
        self.actual_moves_calculated = False
        self.move_template_generated = False

    # Calculates moves available
    def calculate_actual_moves(self, is_in_check):
        theoretical_moves = []
        for values in self.valid_moves.values():
            theoretical_moves.append([value for value in values])
        actual_moves = []
        for theoretical_move in theoretical_moves:
            # Continue if move does not block a currently checked king
            if not (is_in_check and self.is_blocking_check(theoretical_move)):
                continue
            # Continue if piece exposes a check
            if self.is_exposing_check(theoretical_move):
                continue
            # Add theoretical move to actual moves
            actual_moves.append(theoretical_move)
        self.actual_moves = actual_moves
        self.actual_moves_calculated = True

    def get_actual_moves(self):
        if not self.actual_moves_calculated:
            raise Exception("Actual moves cannot be retrieved before being calculated with piece#calculate_actual_moves")
        return self.actual_moves

    # Returns whether or not piece blocks a currently checked king
    def is_blocking_check(self, destination):
        pass

    # Returns whether or not piece exposes a check
    def is_exposing_check(self, destination):
        pass

    def set_position(self, destination):
        self.pos = destination

    # as a result of moving, check which pieces are blocked by this piece
    def update_pieces_blocked(self, board):
        pass

    # as a result of moving, check which pieces are unblocked by this piece
    def update_pieces_unblocked(self, board):
        for piece in board.pieces:
            if piece.team == self.team:
                continue
            for dir in piece.valid_moves:
                if piece.valid_moves[dir][0] == self:
                    # recalc pieces valid moves in dir
                    # store modification
                    break

    # Updates piece's flags after a move occurs
    def update_flags_after_move(self):
        self.actual_moves_calculated = False

    # TODO Steal logic then remove
    # # change valid move directory
    # def _find_valid_moves(self, steps, distance, board):
    #     self.valid_moves = set([])
    #     for step in steps:
    #         # create array with distance number of step values
    #         moves_in_dir = np.array([step for i in range(distance)])
    #         # cumulative sum the step values to create absolute possible moves
    #         moves_in_dir = np.cumsum(moves_in_dir, axis=0)
    #         # center the array around the piece's current location
    #         moves_in_dir = np.array(self.pos).flatten() + moves_in_dir
    #         for i in range(len(moves_in_dir)):
    #             # Break out if current location is off the board
    #             if not board.in_range(moves_in_dir[i]):
    #                 moves_in_dir = moves_in_dir[:i]
    #                 break
    #             # Continue if board location is not occupied
    #             if not board.board[tuple(moves_in_dir[i])]:
    #                 continue
    #             # Break out after adding current move due to collision with enemy
    #             elif board.board[tuple(moves_in_dir[i])].team != self.team:
    #                 moves_in_dir = moves_in_dir[:i+1]
    #                 break
    #             # Break out after adding current move due to collision with teammate
    #             elif board.board[tuple(moves_in_dir[i])].team == self.team:
    #                 moves_in_dir = moves_in_dir[:i]
    #                 break
    #             else:
    #                 raise RuntimeError("Error! Possible move could not be sorted")
    #
    #         for valid_pos in moves_in_dir:
    #             self.valid_moves.add(tuple(valid_pos))




