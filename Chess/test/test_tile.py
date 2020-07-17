from Chess.tile import Tile 
from Chess.board import Board

def test_init_should_set_row():
    test_board = Board()
    testTile = Tile(1,1,test_board,True)
    assert testTile.row == 1

def test_init_should_set_column():
    test_board = Board()
    testTile = Tile(1,1,test_board,True)
    assert testTile.column == 1

def test_init_should_set_board():
    test_board = Board()
    testTile = Tile(1,1,test_board,True)
    assert testTile.board == test_board

def test_init_should_set_is_black():
    test_board = Board()
    testTile = Tile(1,1,test_board,True)
    assert testTile.row == True