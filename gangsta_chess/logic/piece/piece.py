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
        if move[0] >= self.board.shape[0] or move[1] >= self.board.shape[1]:
            return False
        return True

    def _calculate_valid_moves(self, step, dist=999, capture=False):
        current_move = np.array([np.array(self.pos)])
        for i in range(dist):
            current_move += np.array([step])
            if not self._in_range(current_move[0]):
                break
            elif not self.board.board[tuple(current_move[0])].occupied_by:
                if capture:
                    continue
                self.valid_moves = np.append(self.valid_moves, current_move, axis=0)
            elif self.board.board[tuple(current_move[0])].occupied_by.team != self.team:
                self.valid_moves = np.append(self.valid_moves, current_move, axis=0)
                break
            else:
                break

    def _capture(self, position):
        self.board.captured_pieces = np.concatenate((self.board.captured_pieces, [self.board.board[tuple(position)].occupied_by]))
        self.board.pieces = np.delete(self.board.pieces, np.where(self.board.pieces == self))
        self.board.board[tuple(position)].occupied_by.is_captured = True

    def move(self, position):
        for i in self.valid_moves:
            if tuple(i) == tuple(position):
                if self.board.board[tuple(i)].occupied_by:
                    self._capture(i)
                self._update_tiles(False)
                self.board.board[tuple(self.pos)].occupied_by = None
                self.pos = tuple(i)
                self.board.board[tuple(i)].occupied_by = self
                self._find_valid_moves()
                return True
        return False

    def _update_tiles(self, add):
        for i in self.valid_moves:
            if add:
                self.board.board[tuple(i)].can_move_here.add(self)
            else:
                self.board.board[tuple(i)].can_move_here.remove(self)

    def _find_valid_moves(self):
        self.valid_moves = np.array([np.array(self.pos)], dtype=int)




