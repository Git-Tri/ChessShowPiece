from tkinter import Canvas,Tk,mainloop
from Chess.board import Board

tile_size = 70
borderSize = 20
x_gap = 100 
y_gap = 20

def drawBoard(canvas):

    board = Board()

    keys = list(board.board.keys()) 

    for key in keys: 
        x = (key[0]) * tile_size + x_gap + (borderSize/2)
        y = (key[1]) * tile_size + y_gap + (borderSize/2)
        #you need to get the x and y value from the key
        #then get the tile from board.board 
        tile = board.board[key]

        if tile.is_black: 
            
            canvas.create_rectangle(x, y, x + tile_size, y + tile_size,fill="black",outline="")

        else:

            canvas.create_rectangle(x, y, x + tile_size, y + tile_size,fill="white",outline="")
        
        #then set colour based isblack 
        #then remember i told you i had cold you can't be angry at me i told you 
        #then draw the rectangle 
        #kill ryan

def main():
    master = Tk()

    canvas = Canvas(master, width=800, height=600)
    canvas.pack()

    canvas.create_rectangle(x_gap, y_gap, x_gap+(tile_size*8)+(borderSize),
         y_gap+(tile_size*8)+(borderSize),fill="brown",outline="")

    drawBoard(canvas)

    mainloop()


if __name__ == '__main__':
    main()