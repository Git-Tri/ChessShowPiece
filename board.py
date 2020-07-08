from ChessShowPiece.tile import Tile

class Board:

    def __init__(self):
        board = {}
        is_next_black = False
        for row in range(8):
            for column in range(8):                
                board[(row,column)] = Tile(row,column,self,is_next_black)
                is_next_black = not is_next_black
            is_next_black = not is_next_black
        self.board = board
        

