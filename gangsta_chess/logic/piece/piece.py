import numpy as np


class Piece:
    def __init__(self, team, pos):
        self.is_captured = False
     #   self.valid_moves = set([])
        self.valid_moves = {}  # {dir : [moves]}
        self.team = team
        self.pos = pos

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

    # begin game
    # 1. place pieces by moving them onto board as described above (skip theoretical)


    # on a theoretical move check which pieces are blocked by this piece
    def _update_pieces_blocked(self, board):
        pass

    # on a theoretical move check which pieces are unblocked by this piece
    def _update_pieces_unblocked(self, board):
        for piece in board.pieces:
            if piece.team == self.team:
                continue
            for dir in piece.valid_moves:
                if piece.valid_moves[dir][0] == self:
                    # recalc pieces valid moves in dir
                    # store modification
                    break



    # change valid move directory
    def _find_valid_moves(self, steps, distance, board):
        self.valid_moves = set([])
        for step in steps:
            # create array with distance number of step values
            moves_in_dir = np.array([step for i in range(distance)])
            # cumulative sum the step values to create absolute possible moves
            moves_in_dir = np.cumsum(moves_in_dir, axis=0)
            # center the array around the piece's current location
            moves_in_dir = np.array(self.pos).flatten() + moves_in_dir
            for i in range(len(moves_in_dir)):
                # Break out if current location is off the board
                if not board.in_range(moves_in_dir[i]):
                    moves_in_dir = moves_in_dir[:i]
                    break
                # Continue if board location is not occupied
                if not board.board[tuple(moves_in_dir[i])]:
                    continue
                # Break out after adding current move due to collision with enemy
                elif board.board[tuple(moves_in_dir[i])].team != self.team:
                    moves_in_dir = moves_in_dir[:i+1]
                    break
                # Break out after adding current move due to collision with teammate
                elif board.board[tuple(moves_in_dir[i])].team == self.team:
                    moves_in_dir = moves_in_dir[:i]
                    break
                else:
                    raise RuntimeError("Error! Possible move could not be sorted")

            for valid_pos in moves_in_dir:
                self.valid_moves.add(tuple(valid_pos))




