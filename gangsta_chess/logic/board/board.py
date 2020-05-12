import numpy as np
from gangsta_chess.logic.board.tile import Tile


class Board:
    def __init__(self, Pieces, shape):
        self.shape = shape
        self.board = np.array([[Tile() for i in range(shape[1])] for j in range(shape[0])])
        self.pieces = np.empty(0)
        self.captured_pieces = np.empty(0)
