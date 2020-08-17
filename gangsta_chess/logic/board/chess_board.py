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
        self.__init_chess_game()

    def __init_chess_game(self):
        back_row = np.array([Rook, Knight, Bishop, King, Queen, Bishop, Knight, Rook])

        self.board[0] = np.array([back_row[i]('w', (0, i)) for i in range(self.shape[1])])
        self.board[7] = np.array([np.flip(back_row)[i]('b', (7, i)) for i in range(self.shape[1])])
        self.board[1] = np.array([Pawn('w', (1, i)) for i in range(self.shape[1])])
        self.board[6] = np.array([Pawn('b', (6, i)) for i in range(self.shape[1])])
        for i in range(2, 6):
            self.board[i] = np.array([None for i in range(self.board.shape[1])])

        for i in self.board:
            for j in i:
                if j:
                    self.pieces.add(j)

    def move(self, piece_pos, dest_pos):
        piece = self.board[piece_pos]
        dest = self.board[dest_pos]
        if dest_pos not in piece.valid_moves:
            return False
        # if the destination is an enemy piece, capture the enemy piece
        if dest and dest.team != piece.team:
            dest.is_captured = True
            self.board.captured_pieces.add(dest)
        # if the piece is a pawn and the move is successful the next move will not be the first
        if isinstance(piece, Pawn):
            piece.is_first_move = False
        # move the piece
        self.board[piece_pos] = None
        self.board[dest_pos] = piece
        return True


game = ChessBoard(Piece)
print(game)
pos = (1, 3)
move = (2, 3)
game.board[pos].find_valid_moves(game)
game.move(pos, move)
# print(game.board[pos].move(move))
print(game)

