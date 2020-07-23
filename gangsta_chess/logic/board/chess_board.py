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

        self.board[0] = np.array([back_row[i]('w', self) for i in range(self.shape[1])])
        self.board[7] = np.array([np.flip(back_row)[i]('b', self) for i in range(self.shape[1])])
        self.board[1] = np.array([Pawn('w', self) for i in range(self.shape[1])])
        self.board[6] = np.array([Pawn('b', self) for i in range(self.shape[1])])
        for i in range(2, 6):
            self.board[i] = np.array([None for i in range(self.board.shape[1])])

        for i in self.board:
            for j in i:
                if j:
                    self.pieces.add(j)

game = ChessBoard(Piece)

pos = (1, 3)
move = (5, 0)
game.board[pos].move(move)
game.board[pos].find_valid_moves()
print(game.board[pos].valid_moves)
# game.board.pos
# game.board[move].find_valid_moves()
# print(game.board[move].valid_moves())
# game.board[6, 1].find_valid_moves()
# print(game.board[move].in_check())
print(game)
