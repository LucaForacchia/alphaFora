from abc import ABC, abstractmethod

class Move(ABC):
    def __init__(self, from_row, from_col, to_row, to_col):
        self.from_row = from_row
        self.from_col = from_col
        self.to_row = to_row
        self.to_col = to_col

    @abstractmethod
    def is_legal(self, board):
        pass

    @classmethod
    @abstractmethod
    def parse(cls, move_str, board):
        """
        Try to parse move_str; return instance or None
        """
        pass