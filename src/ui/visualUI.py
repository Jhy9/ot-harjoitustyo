import tkinter as tk
from sudoku.game import Game

class VisualUI:

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Sudoku")
        
        menus = tk.Menu(self.root)
        filemenu = tk.Menu(menus)
        filemenu.add_command(label = "Close", command=exit)
        menus.add_cascade(menu=filemenu, label = "File")
        self.root.config(menu= menus)


        self.root.mainloop()