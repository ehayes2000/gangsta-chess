import numpy as np


class Board:
    def __init__(self, shape=(8,8)):
        self.board = np.zeros(shape)
        self.board[0, 1] = 1
        self.board[0, 2] = 1

    def get_pieces(self):
        return np.where(self.board == 1)
