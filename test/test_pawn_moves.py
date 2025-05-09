import pytest
from moves import Move
from pawn_move import PawnMove
from chessboard import ChessBoard

@ pytest.fixture()
def board():
    return ChessBoard()

@ pytest.mark.parametrize("move_str, start_row, start_col, end_row, end_col", [
    ('e3', 6, 4, 5, 4),  # one-step advance
    ('e4', 6, 4, 4, 4),  # two-step advance
    ('e6', 1, 4, 2, 4),  # black one-step advance
])

def test_parse_and_legal_advance(board, move_str, start_row, start_col, end_row, end_col):
    # Fix turn for black test
    board.turn = 'b' if move_str == 'e6' else 'w'
    move = PawnMove.parse(move_str, board)
    assert move is not None
    assert move.from_row == start_row and move.from_col == start_col
    assert move.to_row == end_row and move.to_col == end_col
    assert move.is_legal(board)

def test_illegal_advance_too_far(board):
    board.turn = 'w'
    assert PawnMove.parse('e5', board) is None
    
def test_simple_capture(board):
    # Set up black pawn at d5
    board.board[3][3] = 'p'
    board.turn = 'w'
    move = PawnMove.parse('exd5', board)
    assert move is not None
    assert move.from_row == 4 and move.from_col == 4
    assert move.to_row == 3 and move.to_col == 3
    assert move.is_legal(board)

@ pytest.mark.parametrize('notation', ['exd5', 'fxe6'])
def test_illegal_capture_empty(board, notation):
    board.turn = 'w'
    assert PawnMove.parse(notation, board) is None
