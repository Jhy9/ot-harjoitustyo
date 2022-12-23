import random
from sudoku.board import Board


class SaveManager:
    """Luokka, joka vastaa pelin lataus- ja tallennustoiminnallisuuksista"""
    def load_game(self, file_name):
        """Lataa peliruudukon datan parametrin tekstitiedostosta,
        luo uuden ruudukon datan perusteella ja palauttaa sen"""
        file = file_name
        error_message = "Peliä ei voitu ladata. Tiedoston data vaurioitunut." 
        with open(file,"r", encoding = "utf-8") as reader:
            data = reader.read()
        try:
            game_data = data.split(",")
            board = Board(game_data[0],game_data[1])
        except IndexError:
            print(error_message)
            return Board([0]*81)
        except ValueError:
            print(error_message)
            return Board([0]*81)
        if len(board.board) != 81:
            print(error_message)
            return Board([0]*81)
        return board

    def save_game(self, file_name, board):
        """Tallentaa pelin annettuun hakemistoon omaan tekstitiedostoonsa annettulla nimellä"""
        data = board.give_save_form()
        file = file_name+ ".txt"
        with open(file, "w+", encoding = "utf-8") as writer:
            writer.write(data)

    def new_game(self):
        """Arpoo satunnaisen peliruudukon games.txt tiedostosta ja palauttaa sen.
        Käytetään, kun pelaaja aloittaa uuden pelin"""
        try:
            with open("src/sudoku/games.txt","r",encoding = "utf-8") as reader:
                line = reader.read().splitlines()
        except FileNotFoundError:
            print("Tiedostoa src/sudoku/games.txt ei löytynyt.")
            return Board([0]*81)
        boardstr = random.choice(line)
        if len(boardstr) != 81:
            print("Yritettiin ladata korruptoitunut rivi tiedostosta src/sudoku/games.txt. Lataa tiedosto games.txt uudestaan.")# pylint: disable=line-too-long
            print(len(boardstr))
            return Board([0]*81)
        board = Board(boardstr)
        return board

    def add_new(self, board):
        """Lisää uuden pelin games.txt tiedostoon.
        Peliruudukon voi saada pelattavaksi satunnaisesti, kun käyttäjä aloittaa uuden pelin."""
        with open("src/sudoku/games.txt","a",encoding = "utf-8") as writer:
            board_as_str = str(board)
            writer.write('\n'+board_as_str)
            