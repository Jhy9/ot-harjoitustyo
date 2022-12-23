from sudoku.tile import Tile


class Board:
    """Luokka, joka kuvaa kokonaista peliruudukkoa. Ruudukko koostuu joukosta tile luokan olioita"""
    board = []
    locks = []

    def __init__(self, initial_numbers, locked=None):
        """Konstruktori, joka luo uuden ruudukon. Saa syötteenä ruudukon kaikki arvot
        sekä mahdollisesti tiedon lukituista ruuduista locked parametrissa.
        Täysin uutta peliä aloittaessa luokka itse määrittää lukitut ruudut,
        mutta jos keskeneräinen peli ladataan muistista niin käytetään
        sen pelin alkuperäisesti lukittuja ruutuja(, jotka saadaan locked parametrissa)"""
        self.board = []
        self.locks= []
        if locked is None:
            self._create_new_board(initial_numbers)
        else:
            self._load_board(initial_numbers, locked)

    def _create_new_board(self, numbers):
        #Luodaan uudelle pelille ruudukko
        for num in numbers:
            self.board.append(Tile(num))
            if int(num) > 0:
                self.locks.append(1)
            else:
                self.locks.append(0)

    def _load_board(self, numbers,locks):
        #Luodaan muistista ladatulle keskeneräiselle pelille ruudukko
        size = len(numbers)
        for i in range(size):
            self.board.append(Tile(numbers[i],locks[i]))
            self.locks.append(int(locks[i]))

    def change_value(self, location, new_value):
        #Vaihtaa ruudukon ruudun arvoa
        self.board[location].change_value(new_value)

    def give_array_form(self):
        #Palauttaa ruudukon ruutujen arvot int-arrayna
        board_array = []
        for i in self.board:
            board_array.append(int(i.value))
        return board_array

    def give_save_form(self):
        """Palauttaa ruudukon muodossa (ruudukon sisältö + , + lukotetut ruudut)
        tallennusta varten"""
        board_data= ""
        for i in self.board:
            board_data+= str(i)
        board_data += ","
        for i in self.locks:
            board_data += str(i)
        return board_data

    def __str__(self):
        #Palauttaa vain ruudukon ruutujen arvot string-muodossa
        string_form = ""
        for i in self.board:
            string_form += str(i)
        return string_form
