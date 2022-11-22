from sudoku.board import Board

class TextUI:
    def launchGame(self, boardData):
        board = Board(boardData)
        print("This is temporary ui to test out the game")
        print("Currently there are no checks implemented")
        print("Commands:")
        print("x -  quit")
        print("add xyz - insert value z on board position xy (x and y in range 0:8)")
        print("x goes from left to right and y up to down")
        print("0 means that tile is empty")
        while(True):
            board.print()
            s = input("Enter command:")
            if(s == 'x'):
                break
            
            if(s.startswith("add")):
                x = int(s[4])
                y = int(s[5])
                z = s[6]
                board.changeValue(x+y*9,z)
