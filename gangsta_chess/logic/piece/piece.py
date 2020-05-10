import numpy as np


class Piece:
    def __init__(self, pos, team, Board):
        self.pos = pos
        self.is_captured = False
        self.valid_moves = None # valid moves is made by the specific piece as a 2d numpy array where each array
                                # is the moves that can be taken in one direction
        self.team = team
        self.board = Board


    def _in_range(self, move):
        if move[0] < 0 or move[1] < 0:
            return False
        if move[0] >= self.board.board[:, 0].size or move[1] >= self.board.board[0, :].size:
            return False
        return True

    def _calculate_valid_moves(self, step, dist=999, capture=False):
        current_move = np.array([np.array(self.pos)])
        for i in range(dist):
            current_move += np.array([step])

            if not self._in_range(current_move[0]):
                break

            elif not self.board.board[tuple(current_move[0])]:
                if capture:
                    continue
                self.valid_moves = np.append(self.valid_moves, current_move, axis=0)
            elif self.board.board[tuple(current_move[0])].team != self.team:
                self.valid_moves = np.append(self.valid_moves, current_move, axis=0)
                break
            else:
                break

    def move(self, position):
        # TODO captures
        for i in self.valid_moves:
            if tuple(i) == tuple(position):
                self.board.board[tuple(position)] = self
                self.board.board[self.pos] = None
                self.pos = position
                return True
        return False

    def find_valid_moves(self):
        self.valid_moves = np.array([np.array(self.pos)], dtype=int)





