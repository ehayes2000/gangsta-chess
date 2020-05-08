from gangsta_chess.logic.piece.piece import *


class Queen(Piece):
    def __init__(self, pos, team, Board):
        super().__init__(pos, team, Board)