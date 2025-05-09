from src.moves import Move

class PawnMove(Move):
    
    @classmethod
    def square_to_coords(cls, sq, board):
        if len(sq)!=2 or sq[0] not in board.cols_map or sq[1] not in '12345678':
            return None
        return 8-int(sq[1]), board.cols_map[sq[0]]

    @classmethod
    def parse(cls, move_str, board):
        move = move_str.strip().lower()

        # Simple advance (e.g., 'e4')
        if len(move)==2:
            return PawnMove.advance(move, board)

        # Capture (exd5)
        elif len(move)==4 and move[1]=='x':
            return PawnMove.capture(move, board)
        
        return None
    
    @classmethod
    def advance(cls, move, board):
        # get the destination square
        dst = PawnMove.square_to_coords(move, board)            
        if not dst: return None
        row_to, col_to = dst

        # determine direction of the move (white pawn moves upwards)
        dir = -1 if board.turn=='w' else 1

        # one-step
        row_from = row_to - dir
        if 1<=row_from<6 and ((board.turn=='w' and board.board[row_from][col_to]=='P') or (board.turn=='b' and board.board[row_from][col_to]=='p')):
            return cls(row_from,col_to,row_to,col_to)

        # two-step
        end = 4 if board.turn=='w' else 3
        if row_to==end:
            row_from = row_to - 2*dir
            if (board.turn=='w' and board.board[row_from][col_to]=='P') or (board.turn=='b' and board.board[row_from][col_to]=='p'):
                return cls(row_from,col_to,row_to,col_to)

        return None
    
    @classmethod
    def capture(cls, move, board):
        dst = PawnMove.square_to_coords(move[2:], board)
        col_from = board.cols_map.get(move[0])
        if col_from is None or not dst: return None
        row_to, col_to = dst

        # determine direction of the move (white pawn moves upwards)
        dir = -1 if board.turn=='w' else 1

        row_from = row_to - dir

        if 1<=row_from<8:
            if (board.turn=='w' and board.board[row_from][col_from]=='P') or (board.turn=='b' and board.board[row_from][col_from]=='p'):
                return cls(row_from, col_from, row_to, col_to)
        return None
    
    def is_legal(self, board):
        piece = board.board[self.from_row][self.from_col]
        target = board.board[self.to_row][self.to_col]
        dir = -1 if piece.isupper() else 1
        # advance
        if self.from_col==self.to_col and target=='.':
            if self.to_row - self.from_row == dir:
                return True
            # double
            start = 6 if piece.isupper() else 1
            if self.from_row==start and self.to_row - self.from_row == 2*dir:
                mid = self.from_row + dir
                if board.board[mid][self.from_col]=='.':
                    return True
        # capture
        if abs(self.from_col-self.to_col)==1 and self.to_row-self.from_row==dir:
            if target!='.' and (target.isupper()!=piece.isupper()):
                return True
        return False