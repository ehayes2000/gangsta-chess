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

    # *BEGIN GAME*
    # 1. place pieces by moving them onto board (skip theoretical)

    def __init__(self, shape=(8, 8)):
        super().__init__(Piece, shape)

        # GLOBAL
        self.BACK_ROW = np.array([Rook, Knight, Bishop, King, Queen, Bishop, Knight, Rook])
        self.WHITE = 'w'
        self.BLACK = 'b'

        # Instance
        self.blocking_pieces = {}       # {blocking : (piece, dir)}
        self.reachable_positions = {}   # {move : [piece_1, piece_2], move_2 : [piece_1, piece_2]}

        # FLAGS
        self.pieces_placed = False
        self.team_check = {self.WHITE: False, self.BLACK: False}

    # Place pieces on the chess board
    def place_pieces(self):
        if self.pieces_placed:
            raise RuntimeError("Pieces cannot be placed on the chess board more than once")
        else:
            self.pieces_placed = True

        initial_pieces = np.array(self.shape, dtype=self.piece_type)

        initial_pieces[0] = [[self.BACK_ROW[i](self.WHITE), (0, i)] for i in range(self.shape[1])]
        initial_pieces[7] = [[np.flip(self.BACK_ROW)[i](self.BLACK), (7, i)] for i in range(self.shape[1])]
        initial_pieces[1] = [[Pawn(self.WHITE), (1, i)] for i in range(self.shape[1])]
        initial_pieces[6] = [[Pawn(self.BLACK), (6, i)] for i in range(self.shape[1])]

        for row in initial_pieces:
            for piece_pos in row:
                self.move(piece_pos[0], piece_pos[1], force=True)

    def get_piece_at_position(self, position):
        for piece in self.pieces:
            if piece.pos == position:
                return piece
        return None

    def move(self, piece, destination, force=False):
        if not force:
            if not piece.actual_moves_calculated:
                piece.calculate_actual_moves(self.team_check[piece.team])
            if destination not in piece.actual_moves():
                raise Exception(f"The {piece} cannot move to {destination}")

        piece.set_position(destination)
        piece.update_pieces_blocked(self)
        piece.update_pieces_unblocked(self)
        piece.update_flags_after_move()

    # TODO Steal logic then remove
    # def __init_chess_game(self):
    #     back_row = np.array([Rook, Knight, Bishop, King, Queen, Bishop, Knight, Rook])
    #
    #     self.board[0] = np.array([back_row[i](self.WHITE, (0, i)) for i in range(self.shape[1])])
    #     self.board[7] = np.array([np.flip(back_row)[i](self.BLACK, (7, i)) for i in range(self.shape[1])])
    #     self.board[1] = np.array([Pawn(self.WHITE, (1, i)) for i in range(self.shape[1])])
    #     self.board[6] = np.array([Pawn(self.BLACK, (6, i)) for i in range(self.shape[1])])
    #     for i in range(2, 6):
    #         self.board[i] = np.array([None for i in range(self.board.shape[1])])
    #
    #     for i in self.board:
    #         for j in i:
    #             if j:
    #                 self.pieces.add(j)

    # TODO Steal logic then remove
    # def move(self, piece_pos, dest_pos):
    #     piece = self.board[piece_pos]
    #     dest = self.board[dest_pos]
    #     if dest_pos not in piece.valid_moves:
    #         return False
    #     # if the destination is an enemy piece, capture the enemy piece
    #     if dest and dest.team != piece.team:
    #         dest.is_captured = True
    #         self.board.captured_pieces.add(dest)
    #     # if the piece is a pawn and the move is successful the next move will not be the first
    #     if isinstance(piece, Pawn):
    #         piece.is_first_move = False
    #     # move the piece
    #     self.board[piece_pos] = None
    #     self.board[dest_pos] = piece
    #     piece.pos = dest_pos
    #     return True
    #
    # # find valid move of every piece
    # def find_all_valid_moves(self):
    #     kings = []
    #     # find valid move of every piece if it is not a king
    #     for piece in self.pieces:
    #         if not isinstance(piece, King):
    #             piece.find_valid_moves(self)
    #         else:
    #             kings.append(piece)
    #     # the kings valid moves must be found last because they are dependent on other valid moves
    #     kings[0].find_valid_moves(self)
    #     kings[1].find_valid_moves(self)



game = ChessBoard(Piece)

pos = (1, 3)
move = (2, 3)
game.board[pos].find_valid_moves(game)
game.move(pos, move)

k = King('w')
game.move(k, (4, 3))
r = Rook('b')
game.move(r, (4, 7))
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

