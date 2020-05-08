import numpy as np
from gangsta_chess.logic.piece.piece import Piece
from gangsta_chess.logic.board.board import Board
from gangsta_chess.logic.piece.pawn import Pawn
from gangsta_chess.logic.piece.bishop import Bishop
from gangsta_chess.logic.piece.king import King
from gangsta_chess.logic.piece.knight import Knight
from gangsta_chess.logic.piece.queen import Queen
from gangsta_chess.logic.piece.rook import Rook


class ChessBoard(Board):
    def __init__(self, Pieces, shape=(8, 8)):
        super().__init__(Pieces, shape)
        self.back_row = np.array([Rook, Knight, Bishop, King, Queen, Bishop, Knight, Rook])

    def place_pieces(self):
        self.board[0] = np.array([self.back_row[i]((0, i), 'w', self) for i in range(8)])
        self.board[1] = np.array([Pawn((1, i), 'w', self) for i in range(8)])
        for i in range(2, 6):
            self.board[i] = np.array([None for j in range(self.shape[0])])
        self.board[6] = np.array([Pawn((6, i), 'b', self) for i in range(8)])
        self.board[7] = np.array([np.flip(self.back_row)[i]((7, i), 'b', self) for i in range(8)])