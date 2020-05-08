import numpy as np

class Piece:
    def __init__(self, pos):
        self.pos = pos
        self.is_captured = False
        self.valid_moves = None
        self.team = "W"

    def move(self, pos):
        if pos not in self.valid_moves:
            return False
        else:
            self.pos = pos
            return True

    def get_valid_moves(self):
        if not self.valid_moves:
            self.find_valid_moves()
        return self.valid_moves

    def find_valid_moves(self):
        pass

