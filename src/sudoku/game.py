import math
from sudoku.save_manager import SaveManager
from sudoku.board import Board
class Game:
    """Pelin pääluokka:
    Pitää itsellään pelin ruudukkoa sekä suorittaa ruudukon tarkistukset."""
    board = None
    save_manager = None

    def __init__(self, create = None):
        """Konstruktori, joka ilman konstruktorin parametria hakee
        pelille uuden ruudukon save_manager luokasta.
        Jos konstruktori saa arvon(, eli create ei ole tyhjä), niin siirrytään pelin luomistilaan,
        eli pelaajalle annetaan vain tyhjä ruudukko, jota hän voi täyttää."""
        self.save_manager = SaveManager()
        if create is None:
            self.board = self.save_manager.new_game()
        else:
            self.board = Board([0]*81)

    def load(self, name):
        """Pyytää save_manageria lataamaan ruudukon muistista
        tiedostosta name(parametri) ja tallettaa sen board muuttujaan"""
        self.board = self.save_manager.load_game(name)

    def check_board(self):
        """Tarkistaa onko ruudukossa virheitä tai onko se valmis
        Palauttaa 2, jos ruudukko valmis, 1 jos ei virheitä tai listan ruuduista,
        jotka kuuluvat virheelliseen riviin/sarakkeeseen/3x3 ruutuun"""
        errors = []
        board = self.board.give_array_form()
        errors += self._check_rows(board)
        errors+=self._check_columns(board)
        errors += self._check_squares(board)
        if not errors:
            if self._check_win(board)== 1:
                return 2
            return 1
        return errors

    def _check_rows(self, board):
        """Tarkistaa rivit virheiden varalta"""
        #Palauttaa ruudut, jotka kuuluvat virheellisiin riveihin
        errors = []
        for j in range(9):
            counts = [0]*10
            for i in range(9):
                counts[board[j*9+i]] +=1
            if self._array_check(counts) == 0:
                errors += self._tile_marker(1,j*9)
        return errors

    def _check_columns(self, board):
        """Tarkistaa ruudukon sarakkeet virheiden varalta"""
        #Palauttaa ruudut, jotka kuuluvat virheellisiin sarakkeisiin
        errors = []
        for i in range(9):
            counts = [0]*10
            for j in range(9):
                counts[board[j*9+i]] +=1
            if self._array_check(counts) == 0:
                errors += self._tile_marker(2,i)
        return errors

    def _check_squares(self, board):
        """Tarkistaa 3x3 ruudut virheiden varalta"""
        #Palauttaa ruudut, jotka kuuluvat virheellisiin 3x3 ruudukkoihin
        errors = []
        for i in range (9):
            counts = [0]*10
            for j in range (9):
                counts[board[math.floor(i/3)*27+i%3*3+j%3+math.floor(j/3)*9]] += 1
            if self._array_check(counts) == 0:
                errors += self._tile_marker(3, math.floor(i/3)*27+i%3*3)
        return errors

    def _check_win(self, board):
        """Jos ruudukossa ei ole yhtään nollaa(eli tyhjiä ruutuja) ja virheitä ei ole, on peli
            voitettu
            Saa syötteenä peliruudukon"""
        for i in range(81):
            if board[i]==0:
                return 0
        return 1

    def _array_check(self, array):
        """Tarkastaa, onko virhe tapahtunut:
        Jos rivillä/sarakkeella/ruudukolla on kaksi samaa numeroa, niin se on virhe.
        Saa syötteenä arrayn, jossa on kunkin numeron/tyhjän ruudun ilmaantumisten määrä."""
        #Palauttaa 0 jos on virhe ja 1 jos ei
        for i in range (1,10):
            if array[i] > 1:
                return 0
        return 1

    def _tile_marker(self, tiles, start):
        """Palauttaa virheelliset ruudut
        Saa syötteenä merkittävän ruutukokoelman tyypin sekä aloitusindeksin"""
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
