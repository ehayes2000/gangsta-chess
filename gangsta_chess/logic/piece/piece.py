import numpy as np


class Piece:
    def __init__(self, pos, team, Board):
        self.pos = pos
        self.is_captured = False
        self.valid_moves = None # valid moves is made by the specific piece as a 2d numpy array where each array
                                # is the moves that can be taken in one direction
        self.team = team
        self.board = Board
        self.relative_dir = 1 if self.team == 'w' else -1

    def move_up_down(self, dist, dir=1):
        temp_pos = np.array(self.pos)
        for i in range(dist):
            temp_pos[0] += dir
            try:
                if not self.board.board[tuple(temp_pos)]:
                    self.valid_moves = np.concatenate((self.valid_moves, temp_pos))
                elif self.board.board[tuple(temp_pos)].team != self.team:
                    self.valid_moves = np.concatenate((self.valid_moves, temp_pos))
                    break
                else:
                    break
            except IndexError:
                break
        self.valid_moves = self.valid_moves.reshape((int(len(self.valid_moves) / 2), 2))






