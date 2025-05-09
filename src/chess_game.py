from src.pawn_move import PawnMove  # add more as implemented
from src.chessboard import ChessBoard

# Orchestrates parsing and executing moves

class ChessGame:
    def __init__(self):
        self.board = ChessBoard()
        self.move_classes = [PawnMove]  # extend with KnightMove, etc.

    def parse_move(self, move_str):
        for cls in self.move_classes:
            mv = cls.parse(move_str, self.board)
            if mv and mv.is_legal(self.board):
                return mv
        return None

    def play(self):
        self.show_board = True
        while True:
            if self.show_board:
                self.board.display()
            move_str = input("Enter move (or 'quit'): ").strip()
            if move_str.lower()=='quit': break
            mv = self.parse_move(move_str)
            if mv:
                self.board.apply_move(mv)
                self.show_board = True
            else:
                print("Invalid or illegal move.")
