from sudoku.game import Game


class TextUI:
    def launchGame(self):
        game = Game()
        print("This is temporary ui to test out the game")
        print("Currently there are no checks implemented")
        print("Commands:")
        print("x -  quit")
        print("add xyz - insert value z on board position xy (x and y in range 0:8)")
        print("save name - saves game into name")
        print("load name - loads game from name")
        print("new - starts new game with random board")
        print("x goes from left to right and y up to down")
        print("0 means that tile is empty")
        while (True):
            board = str(game.board)
            i = 0
            s = ""
            for x in board:
                s += str(x) + " "
                i += 1
                if i == 9:
                    i = 0
                    print(s)
                    s = ""

            s = input("Enter command:")
            if (s == 'x'):
                break

            if (s.startswith("add")):
                x = int(s[4])
                y = int(s[5])
                z = s[6]
                game.board.change_value(x+y*9, z)
                board_check = game.check_board()
                if board_check == 1:
                    continue
                if board_check == 2:
                    print("You win!")
                if len(board_check) > 1:
                    print("Error in tiles:")
                    print(board_check)

            if (s.startswith("load")):
                command = s.split(" ")
                game.load(command[1])

            if (s.startswith("save")):
                command = s.split(" ")
                game.save(command[1])

            if(s == "new"):
                game = Game()


