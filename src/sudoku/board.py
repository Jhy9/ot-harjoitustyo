from sudoku.tile import Tile


class Board:
    board = []
    def __init__(self, initialNumbers):
        for x in initialNumbers:
            self.board.append(Tile(x))



    def changeValue(self, location, newValue):
        self.board[location].changeValue(newValue)


    def print(self):
        i = 0
        s = ""
        for x in self.board:
            s += str(x)+ " "
            i += 1
            if i == 9:
                i = 0
                print(s)
                s = ""                


    def __str__(self):
        s = ""
        for i in self.board:
            s += str(i)
        return s