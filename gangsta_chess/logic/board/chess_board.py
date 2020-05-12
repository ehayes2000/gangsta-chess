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
        self._place_pieces()
        self._find_all_valid_moves()

    def _place_pieces(self):
        self.pieces = np.concatenate((self.pieces, np.array([self.back_row[i]((0, i), 'w', self) for i in range(8)])))
        self.pieces = np.concatenate((self.pieces, np.array([Pawn((1, i), 'w', self) for i in range(8)])))
        self.pieces = np.concatenate((self.pieces, np.array([Pawn((6, i), 'b', self) for i in range(8)])))
        self.pieces = np.concatenate((self.pieces, np.array([np.flip(self.back_row)[i]((7, i), 'b', self) for i in range(8)])))
        for piece in self.pieces:
            self.board[piece.pos].occupied_by = piece

    def _find_all_valid_moves(self):
        for i in self.pieces:
            i._find_valid_moves()


game = ChessBoard(Piece)
bPiece = King((3, 4), 'b', game)
game.board[3, 4].occupied_by = bPiece
game.board[3, 4].occupied_by._find_valid_moves()


# print(game.board[1, 0].)
# FIXME anytime any piece moves, all pieces must update valid moves,
# anytime a piece moves update moves for pieces that could previously move
# where the piece moved to or from


