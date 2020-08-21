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
        self.theoretical_moves = {}  # {dir : [moves]}
        self.move_template = move_template  # [[dir_1], [dir_2], ... , [dir_n]]
        self.actual_moves = []

        # FLAGS
        self.actual_moves_calculated = False
        self.move_template_generated = False


    # Generates pieces move template
    def _generate_move_template(self, steps, distance, board):
        self.move_template = 0
        # TODO Generate move template
        self.move_template_generated = True

    # Returns whether or not a move will put the king out of check if currently in check
    # relevant_blocking_pieces = pieces being blocked by king
    def _will_block_check(self, destination, pieces_blocked_by_king):
        for pairs in pieces_blocked_by_king:
            for piece, direction in pairs:
                if destination in piece.theoretical_moves[direction] and piece.team != self.team:
                    continue
                else:
                    return False
        return True

    # Returns whether or not piece exposes a check
    # pieces_being_blocked = all pieces being blocked by current piece
    # TODO doesn't work when blocking piece is a pawn because pawns can only move 1
    # TODO King must be able to move on top of friendly pieces in the reachable_positions dict
    def _will_expose_check(self, destination, pieces_being_blocked, reachable_positions, team_king):
        # if the current piece blocks no pieces, no move it can take can expose check
        if not pieces_being_blocked:
            return False
        # if the king does not have LOS to the current piece it cannot expose check
        if team_king not in reachable_positions[self.pos]:
            return False
        # find the direction away from the current piece to the king
        opposite_king_block_dir = None
        for piece, dir in pieces_being_blocked:
            if not piece is team_king:
                continue
            opposite_king_block_dir = -1 * np.array(dir)
            break
        # is the current piece blocking any piece in the direction to the king
        for piece, dir in pieces_being_blocked:
            if dir == opposite_king_block_dir and piece.team != self.team:
                direction = np.array(self._find_relative_direction(piece))
                # if the move will keep the current piece between the enemy it is blocking and the king return False
                if direction == opposite_king_block_dir or direction == -1 * opposite_king_block_dir:
                    return False
                else:
                    return True
        return False

    def _find_relative_direction(self, piece):
        direction = abs(self.pos - piece.pos)
        if direction[0] != 0:
            direction[0] = direction[0] / abs(direction[0])
        if direction[1] != 0:
            direction[1] = direction[1] / abs(direction[1])
        return tuple(direction)

        # Returns pieces move template
    def get_move_template(self):
        if not self.move_template_generated:
            raise Exception("Move template requested but not yet generated. Please ensure "
                            "piece#generate_move_template is called")
        return self.move_template

    # Calculates moves available
    # TODO reference board instead of 4 args
    def calculate_actual_moves(self, is_in_check, pieces_being_blocked, reachable_positions, team_king):
        theoretical_moves = []
        for values in self.theoretical_moves.values():
            theoretical_moves.append([value for value in values])
        actual_moves = []
        for theoretical_move in theoretical_moves:
            # Continue if move does not block a currently checked king
            if not (is_in_check and self._will_block_check(theoretical_move)):
                continue
            # Continue if piece exposes a check
            if self._will_expose_check(theoretical_move, pieces_being_blocked, reachable_positions, team_king):
                continue
            # Add theoretical move to actual moves
            actual_moves.append(theoretical_move)
        self.actual_moves = actual_moves
        self.actual_moves_calculated = True

    def get_actual_moves(self):
        if not self.actual_moves_calculated:
            raise Exception("Actual moves cannot be retrieved before being calculated with piece#calculate_actual_moves")
        return self.actual_moves

    def set_position(self, destination):
        self.pos = destination

    # as a result of moving, check which pieces are blocked by this piece
    # change theoretical moves of pieces being blocked
    # change board's blocked_pieces
    # change board's reachable_positions
    # update blocking_pieces then theoretical_moves then reachable_positions
    # TODO Overide for pawn
    def move(self, board, destination):
        for piece in board.reachable_positions[self.pos]:
            direction = self._find_relative_direction(piece)
            distance_to_wall = 8

            for i in range(distance_to_wall):
                next = piece.theoretical_moves[direction][-1] + np.array(direction)
                if




        board.blocking_pieces[self] = []
        for piece in board.reachable_positions[destination]:
            # find direction between piece being blocked and current
            direction = self._find_relative_direction(piece)
            # update blocked dictionary
            board.blocking_pieces.append((piece, direction))
            # update theoretical moves of the piece that was just blocked

            index = None
            for move in piece.theoretical_moves[direction]:
                if move == destination:
                    index = move
                    break
            if piece.team != self.team:
                piece.theoretical_moves[direction] = piece.theoretical_moves[direction][:index + 1]
            else:
                piece.theoretical_moves[direction] = piece.theoretical_moves[direction][:index]

    # as a result of moving, check which pieces are unblocked by this piece
    def update_pieces_unblocked(self, board):
        pass

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




