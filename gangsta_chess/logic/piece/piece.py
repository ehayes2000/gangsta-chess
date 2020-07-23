import numpy as np


class Piece:
    def __init__(self, team, Board):
        self.is_captured = False
        self.valid_moves = set([])
        self.team = team
        self.board = Board

    def move(self, pos):
        if pos not in self.valid_moves:
            return False
        dest_ = self.board.board[pos]
        # if the destination is a friendly piece we cannot move there
        if dest_ and dest_.team == self.team:
            return False
        # if the destination is an enemy piece, capture the enemy piece
        elif dest_ and dest_.team != self.team:
            dest_.is_captured = True
            self.board.captured_pieces.add(dest_)
        # move the piece
        self.board.board[self.pos()] = None
        self.board.board[pos] = self
        return True

    def pos(self):
        if self.is_captured:
            return -1
        return np.where(self.board.board == self)

    def _in_range(self, move):
        if move[0] < 0 or move[1] < 0:
            return False
        if move[0] >= self.board.board[:, 0].size or move[1] >= self.board.board[0, :].size:
            return False
        return True

    # goes 1 less than distance error
    def _find_valid_moves(self, steps, distance):
        self.valid_moves = set([])
        for step in steps:
            moves_in_dir = np.array([step for i in range(distance)])
            moves_in_dir = np.cumsum(moves_in_dir, axis=0)
            moves_in_dir = np.array(self.pos()).flatten() + moves_in_dir
            for i in range(len(moves_in_dir)):
                if not self._in_range(moves_in_dir[i]):
                    moves_in_dir = moves_in_dir[:i]
                    break
                if not self.board.board[tuple(moves_in_dir[i])]:
                    continue
                elif self.board.board[tuple(moves_in_dir[i])].team != self.team:
                    moves_in_dir = moves_in_dir[:i+1]
                    break
                else:
                    moves_in_dir = moves_in_dir[:i]
                    break
            for valid_pos in moves_in_dir:
                self.valid_moves.add(tuple(valid_pos))




