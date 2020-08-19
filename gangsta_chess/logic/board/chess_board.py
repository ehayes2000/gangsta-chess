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
    def __init__(self, pieces, shape=(8, 8)):
        super().__init__(pieces, shape)
        self.__init_chess_game()
        self.blocking = {blocking : (piece, dir)}
        self.can_move = {move : [piece_1, piece_2], move_2 : [piece_1, piece_2]}


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
        piece.pos = dest_pos
        return True

    # find valid move of every piece
    def find_all_valid_moves(self):
        kings = []
        # find valid move of every piece if it is not a king
        for piece in self.pieces:
            if not isinstance(piece, King):
                piece.find_valid_moves(self)
            else:
                kings.append(piece)
        # the kings valid moves must be found last because they are dependent on other valid moves
        kings[0].find_valid_moves(self)
        kings[1].find_valid_moves(self)



game = ChessBoard(Piece)

pos = (1, 3)
move = (2, 3)
game.board[pos].find_valid_moves(game)
game.move(pos, move)

k = King('w', (4, 3))
r = Rook('b', (4, 7))
game.board[4, 3] = k
game.board[4, 7] = r
game.pieces.add(r)
game.pieces.add(k)

# TODO board should find all valid moves of every piece
game.find_all_valid_moves()
k.find_valid_moves(game)
print(k.in_check(game))
print(k.valid_moves)

print(k.in_check_mate)
print(game)

