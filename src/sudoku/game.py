import math
from sudoku.save_manager import Save_manager
class Game:
    board = None

    def __init__(self, board):
        self.board = board

    def save(self, name):
        saver = Save_manager()
        saver.save_game(name, self.board)

    def check_board_values(self):
        """Tarkistaa, että ruutujen sisällöt ovat oikeanlaisia"""
        for tile in self.board:
            if int(tile.value) not in range (10):
                return 0
        return 1

    def check_board(self):
        """Tarkistaa onko ruudukossa virheitä tai onko se valmis
        Palauttaa 2, jos ruudukko valmis, 1 jos ei virheitä tai listan ruuduista,
        jotka kuuluvat virheelliseen riviin/sarakkeeseen/3x3 ruutuun"""
        errors = []
        board = self.board.give_array_form()
        errors.append(self.check_rows(board))
        errors.append(self.check_columns(board))
        errors.append(self.check_squares(board))
        if errors == [[],[],[]]:
            if self.check_win(board)== 1:
                return 2
            return 1
        return errors

    def check_rows(self, board):
        """Tarkistaa rivit virheiden varalta"""
        #Palauttaa ruudut, jotka kuuluvat virheellisiin riveihin
        errors = []
        for j in range(9):
            counts = [0]*10
            for i in range(9):
                counts[board[j*9+i]] +=1
            if self.array_check(counts) == 0:
                errors.append(self.tile_marker(1,j*9))
        return errors

    def check_columns(self, board):
        """Tarkistaa ruudukon sarakkeet virheiden varalta"""
        #Palauttaa ruudut, jotka kuuluvat virheellisiin sarakkeisiin
        errors = []
        for i in range(9):
            counts = [0]*10
            for j in range(9):
                counts[board[j*9+i]] +=1
            if self.array_check(counts) == 0:
                errors.append(self.tile_marker(2,i))
        return errors

    def check_squares(self, board):
        """Tarkistaa 3x3 ruudut virheiden varalta"""
        #Palauttaa ruudut, jotka kuuluvat virheellisiin 3x3 ruudukkoihin
        errors = []
        for i in range (9):
            counts = [0]*10
            for j in range (9):
                counts[board[math.floor(i/3)*27+i%3*3+j%3+math.floor(j/3)*9]] += 1
            if self.array_check(counts) == 0:
                errors.append(self.tile_marker(3, math.floor(i/3)*27+i%3*3))
        return errors

    def check_win(self, board):
        """Jos ruudukossa ei ole yhtään nollaa(eli tyhjiä ruutuja) ja virheitä ei ole, on peli
            voitettu"""
        for i in range(81):
            if board[i]==0:
                return 0
        return 1

    def array_check(self, array):
        """Tarkastaa, onko virhe tapahtunut:
        Jos rivillä/sarakkeella/ruudukolla on kaksi samaa numeroa, niin se on virhe"""
        #Palauttaa 0 jos on virhe ja 1 jos ei
        for i in range (1,10):
            if array[i] > 1:
                return 0
        return 1

    def tile_marker(self, tiles, start):
        """Palauttaa virheelliset ruudut"""
        #tiles 1 = rivi, tiles 2 = sarake, tiles 3 = 3x3 ruudukko
        faulty_tiles = []
        if tiles == 1:
            for i in range(9):
                faulty_tiles.append(start+i)
        if tiles == 2:
            for i in range(9):
                faulty_tiles.append(start+9*i)
        if tiles == 3:
            for i in range(9):
                faulty_tiles.append(start+i%3+math.floor(i/3)*9)
        return faulty_tiles
