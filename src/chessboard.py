class ChessBoard:
    def __init__(self):
        self.board = self.create_starting_position()
        self.turn = 'w'
        self.cols_map = {'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7}

    def create_starting_position(self):
        return [
            list("rnbqkbnr"),
            ["p"]*8,
            ["."]*8,
            ["."]*8,
            ["."]*8,
            ["."]*8,
            ["P"]*8,
            list("RNBQKBNR"),
        ]

    def display(self):
        print("  +------------------------+")
        for i, row in enumerate(self.board):
            print(f"{8-i} | {' '.join(row)} |")
        print("  +------------------------+")
        print("    a b c d e f g h")
        print(f"\nTurn: {'White' if self.turn=='w' else 'Black'}\n")

    def apply_move(self, move):
        piece = self.board[move.from_row][move.from_col]
        self.board[move.to_row][move.to_col] = piece
        self.board[move.from_row][move.from_col] = '.'
        self.turn = 'b' if self.turn=='w' else 'w'


# Test
if __name__ == "__main__":
    board = ChessBoard()
    board.display()

    board.move_piece(6, 4, 4, 4)  # e2 → e4
    board.display()

    board.move_piece(1, 3, 3, 3)  # d7 → d5
    board.display()

    board.move_piece(4, 4, 3, 3)  # e4 × d5 (cattura diagonale) – dovrebbe fallire (nessun pezzo lì)
    board.display()

    board.move_piece(4, 4, 3, 4)  # e4 → e5
    board.display()