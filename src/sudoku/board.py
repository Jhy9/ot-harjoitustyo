from sudoku.tile import Tile


class Board:
    board = []
    locks = []

    def __init__(self, initial_numbers):
        for num in initial_numbers:
            self.board.append(Tile(num))
            if int(num) > 0:
                self.locks.append(1)
            else:
                self.locks.append(0)

    def change_value(self, location, new_value):
        self.board[location].change_value(new_value)

    def give_array_form(self):
        board_array = []
        for i in self.board:
            board_array.append(int(i.value))
        return board_array

    def __str__(self):
        string_form = ""
        for i in self.board:
            string_form += str(i)
        return string_form
