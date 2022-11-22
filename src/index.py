from sudoku.board import Board
from ui.textUI import TextUI

def Main():
    testString = "000005309000270040100904020700000402000006100002050070031007960005000001900000000"
    ui = TextUI()
    ui.launchGame(testString)


if __name__ == "__main__":
    Main()