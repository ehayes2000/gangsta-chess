import numpy as np


class Piece:
    def __init__(self, team, pos):
        self.is_captured = False
        self.valid_moves = set([])
        self.team = team
        self.pos = pos

    # goes 1 less than distance error
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




