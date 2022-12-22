import random
from sudoku.board import Board


class SaveManager:
    def load_game(self, file_name):
        file = file_name
        with open(file,"r", encoding = "utf-8") as reader:
            data = reader.read()
        game_data = data.split(",")
        board = Board(game_data[0],game_data[1])
        return board

    def save_game(self, file_name, board):
        data = board.give_save_form()
        file = file_name+ ".txt"
        with open(file, "w+", encoding = "utf-8") as writer:
            writer.write(data)

    def new_game(self):
        with open("src/sudoku/games.txt","r",encoding = "utf-8") as reader:
            line = reader.read().splitlines()
            board = Board(random.choice(line))
        return board

    def add_new(self, board):
        with open("src/sudoku/games.txt","a",encoding = "utf-8") as writer:
            board_as_str = str(board)
            writer.write('\n'+board_as_str)
            