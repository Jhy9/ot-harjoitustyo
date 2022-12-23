import tkinter as tk
from tkinter import filedialog
import math
from sudoku.game import Game

class GameView:
    """Luokka, joka vastaa pelin käyttöliittymästä"""
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
        creatormenu = tk.Menu(menus)
        filemenu.add_command(label= "Uusi peli", command = self.start_new_game)
        filemenu.add_command(label= "Lataa", command = self.load_game)
        filemenu.add_command(label= "Tallenna", command = self.save_game)
        filemenu.add_command(label = "Sulje", command=exit)
        creatormenu.add_command(label = "Tyhjennä", command = self.empty_board)
        creatormenu.add_command(label = "Tallenna uudeksi", command = self.save_board)
        menus.add_cascade(menu=filemenu, label = "Valikko")
        menus.add_cascade(menu=creatormenu, label = "Pelin luonti")
        self.root.config(menu= menus)
        self.createBoard()
        self.root.mainloop()

    def start_new_game(self):
        """Luo uuden pelin ja sen jälkeen aloittaa sen kutsumalla uudestaan createBoard() metodia"""
        self.game = Game()
        self.createBoard()

    def empty_board(self):
        """Sama kuin edellä paitsi että aloitetaan täysin tyhjällä ruudukolla (käytetään pelin luomiseen)"""
        self.game = Game("new")
        self.createBoard()

    def createBoard(self):
        # Luo peliruudukon
        self.tiles = [0]*81
        for i in range(9):
            square = tk.Frame(self.root)
            square.grid(row = math.floor(i/3), column = i%3)
            square.configure(highlightbackground= 'black')
            square.configure(highlightthickness= 4)
            for j in range(9):
                """Indeksi joudutaan laskemaan, koska ui lisää ruudut 3x3 ruutu kerrallaan kun taas
                luokan Board oliossa ruudut ovat järjestetty rivi kerrallaan"""
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
                self.tiles[index]=tile
                tile.bind('<KeyPress>', lambda event, arg=index: self.set_value(event, arg))

    def set_value(self, event, index):
        """Sijoittaa näppäimenpainallus eventistä saadun arvon ruutuun ja sen jälkeen kutsuu game-luokkaa tarkastamaan
        ruudukon. Jos ruudukossa on virheitä tai ruudukko on valmis, kutsutaan määrättyjä metodeja jatkotoimenpiteisiin."""
        self.repaint()
        self.tiles[index].delete(1.0, 'end')
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
        #Jos peli on voitettu, kaikki ruudut värjätään vihreäksi
        for tile in self.tiles:
            tile.configure(bg = 'lightgreen')

    def paint_errors(self, errors):
        #Värjää kaikki virheelliset rivit/sarakkeet/3x3 ruudut punaisiksi
        #Ei värjää lukittuja ruutuja
        for i in errors:
            if self.game.board.locks[i] == 0:
                self.tiles[i].configure(bg = 'pink')

                    
    def repaint(self):
        #Värjää kaikki ruudut lähtöasetelmaan. 
        #Tarpeellinen virheellisten ruutujen värin poistamiseksi
        i = 0
        for tile in self.tiles:
            if self.game.board.locks[i]==0:
                tile.configure(bg = 'white')
            i+= 1

    def load_game(self):
        #Lataa pelin tiedostosta
        filename = filedialog.askopenfilename(initialdir  = "src/Savegame", title= "Lataa")
        self.game.load(filename)
        self.createBoard()

    def save_game(self):
        #Tallentaa pelin kansioon .txt muotoiseksi tiedostoksi
        filename = filedialog.asksaveasfilename(initialdir= "src/Savegame", title= "Tallenna")
        self.game.save_manager.save_game(filename,self.game.board)

    def save_board(self):
        #Tallentaa peliruudukon games.txt tiedostoon
        self.game.save_manager.add_new(self.game.board)