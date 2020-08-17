import numpy as np


class Board:
    def __init__(self, Pieces, shape):
        self.shape = shape
        self.board = np.empty(shape, dtype=Pieces)
        self.pieces = set([])
        self.captured_pieces = set([])

    def __str__(self):
        print(end='  ')
        for i in range(self.shape[0]):
            print(i, end='  ')
        print(end='\n')
        for i in range(self.shape[0]):
            print(i, end=' ')
            for j in range(self.shape[1]):
                if self.board[i, j]:
                    print(self.board[i, j], end='  ')
                else:
                    print('□', end='  ')
            print(end='\n')
        return ''

    # Check position is on chess board
    def in_range(self, pos):
        if pos[0] < 0 or pos[1] < 0:
            return False
        if pos[0] >= self.board[:, 0].size or pos[1] >= self.board[0, :].size:
            return False
        return True


