from src.chess_move import ChessMove  # add more as implemented
from src.chessboard import ChessBoard

# Orchestrates parsing and executing moves

class ChessGame:
    def __init__(self):
        self.board = ChessBoard()

    def play(self):
        self.show_board = True
        while True:
            if self.show_board:
                self.board.display()
            move_str = input("Enter move ('h' for help, 'quit' to exit): ").strip()
            if move_str.lower()=='quit': break
            elif move_str.lower() in ['h', 'help', '-h', '--help']: 
                print('Format your move as: starting_square-ending_square (for instance, b1-c3)')
                self.show_board=False
                continue
            try:
                mv = ChessMove.parse(move_str, self.board)
                mv.is_legal(self.board)
                self.board.apply_move(mv)
                self.show_board = True
            except Exception as e:
                print(f"Exception {type(e)}, {e}")
                self.show_board = False
