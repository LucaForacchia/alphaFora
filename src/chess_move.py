class ChessMove():
    def __init__(self, from_row, from_col, to_row, to_col):
        self.from_row = from_row
        self.from_col = from_col
        self.to_row = to_row
        self.to_col = to_col

    @classmethod
    def parse(cls, move_str, board):
        '''
            Expected format: e2-e4
        '''
        move = move_str.strip().lower().replace(' ', '')

        if (len(move) != 5 or move[2]!='-'):
            raise MalformedMoveError(move_str)

        from_row, from_col = board.square_to_coords(move[:2])
        to_row, to_col = board.square_to_coords(move[-2:])

        return ChessMove(from_row, from_col, to_row, to_col)

    def is_legal(self, chessboard):
        piece = chessboard.board[self.from_row][self.from_col]
        if piece == '.':
            raise IllegalMoveError("No piece in the starting square")
        elif ((chessboard.turn=="w" and piece in 'rnbkqp') or (chessboard.turn=='b' and piece in 'RNBKQP')):
            raise IllegalMoveError(f"It's {chessboard.turn} turn!")

        else:   
            # For each piece, I should check whether the move is a legal one!! 
            pass

class MalformedMoveError(ValueError):
    def __init__(self, move_str):
        message = f"Bad move format: '{move_str}'"
        super().__init__(message)
        self.move_str = move_str

class IllegalMoveError(ValueError):
    def __init__(self, message):
        message = f"Illegal move: {message}"
        super().__init__(message)
