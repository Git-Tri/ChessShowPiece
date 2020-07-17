from Chess.board import Board
from Chess.tile import Tile
import pytest

def test_board_is_a_dict():
    board = Board()
    assert isinstance(board.board,dict)

def test_board_is_correct_length():
    board = Board()
    assert len(board.board) == 64

    #that the rows starting colour alternates 

test_case_indexes = []

for row in range(8):
        for column in range(8):                
            test_case_indexes.append((row,column))

parametrizeBoard = Board()

@pytest.mark.parametrize("index", test_case_indexes)
def test_board_does_index_exist(index):
    board = parametrizeBoard
    assert isinstance(board.board[index],Tile)

def test_board_should_have_correct_number_of_white():
    board = Board() 
    count = sum([int(not t.is_black) for t in list(board.board.values())])
    assert count == 32

def test_board_should_have_correct_number_of_black():
    board = Board() 
    count = sum([int(t.is_black) for t in list(board.board.values())])
    assert count == 32

test_case_colour_indexes = []
is_black = False

for row in range(8):
    test_case_colour_indexes.append(((row,0),is_black))
    is_black = not is_black

@pytest.mark.parametrize("index,is_black", test_case_colour_indexes)
def test_board_should_have_correct_first_colours(index,is_black):
    assert parametrizeBoard.board[index].is_black == is_black
     