import tkinter as tk
import math
from sudoku.game import Game

class GameView:
    game = None
    root = None
    tiles = []
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Sudoku")
        self.root.geometry('300x310')
        self.game = Game()
        menus = tk.Menu(self.root)
        filemenu = tk.Menu(menus)
        filemenu.add_command(label= "Uusi peli", command = self.start_new_game)
        filemenu.add_command(label = "Sulje", command=exit)
        menus.add_cascade(menu=filemenu, label = "File")
        self.root.config(menu= menus)
        self.createBoard()
        self.root.mainloop()

    def createBoard(self):
        # Luo peliruudukon
        self.tiles = []
        for i in range(9):
            square = tk.Frame(self.root)
            square.grid(row = math.floor(i/3), column = i%3)
            square.configure(highlightbackground= 'black')
            square.configure(highlightthickness= 4)
            for j in range(9):
                index = math.floor(i/3)*27+i%3*3+math.floor(j/3)*9+j%3
                tile = tk.Text(square, height = 1, width = 2, bg = 'white')
                tile.grid(row = math.floor(j/3), column= j%3) 
                value_to_insert = self.game.board.give_array_form()[index]
                if value_to_insert != 0:
                    tile.insert('end',value_to_insert)
                    if self.game.board.locks[index] == 1:
                        tile.configure(bg = 'lightyellow')
                        tile.configure(state = 'disabled')
                tile.configure(font=("Arial", 16))
                self.tiles.append(tile)
                tile.bind('<KeyPress>', lambda event, arg=index: self.set_value(event, arg))

    def start_new_game(self):
        self.game = Game()
        self.createBoard()

    def set_value(self, event, index):
        self.repaint()
        tilei = index%9
        tilej = math.floor(index/9)
        tileind = math.floor(tilej/3)*27+tilej%3*3+math.floor(tilei/3)*9+tilei%3
        self.tiles[tileind].delete(1.0, 'end')
        if event.keysym == 'BackSpace':
            self.game.board.change_value(index, 0)            
        else:
            self.game.board.change_value(index, event.keysym)
        errors = self.game.check_board()
        if errors == 2:
            self.paint_victory()
        elif errors != 1:
            self.paint_errors(errors)

    def paint_victory(self):
        #Jos peli on voitettu, ruutu värjätään vihreäksi
        for tile in self.tiles:
            tile.configure(bg = 'lightgreen')

    def paint_errors(self, errors):
        #Värjää kaikki virheelliset rivit/sarakkeet/3x3 ruudut punaisiksi
        #Ei värjää lukittuja ruutuja
        for x in errors:
            for a in x:
                for i in a:
                    if self.game.board.locks[i] == 0:
                        tilei = i%9
                        tilej = math.floor(i/9)
                        tileind = math.floor(tilej/3)*27+tilej%3*3+math.floor(tilei/3)*9+tilei%3
                        self.tiles[tileind].configure(bg = 'pink')

                    
    def repaint(self):
        #Värjää kaikki ruudut lähtöasetelmaan. 
        #Tarpeellinen virheellisten ruutujen värin poistamiseksi
        i = 0
        for tile in self.tiles:
            gameind = math.floor(i/27)*27+math.floor(i%27/9)*3+i%3+math.floor(i%9/3)*9
            if self.game.board.locks[gameind]==0:
                tile.configure(bg = 'white')
            i+= 1



