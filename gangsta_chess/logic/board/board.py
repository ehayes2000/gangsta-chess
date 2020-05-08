import numpy as np


class Board:
    def __init__(self, Pieces, shape):
        self.shape = shape
        self.board = np.empty(shape, dtype=Pieces)


    def get_pieces(self):
        return np.where(self.board != 1)

    def place_pieces(self):
        pass