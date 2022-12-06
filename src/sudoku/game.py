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
        zeros = 0
        temp = [0]*10
        board_string = self.board.give_array_form()
        for row in range(9):
            #Tarkistaa rivit
            for i in range(9):
                temp[board_string[row*9+i]] += 1
            zeros += temp[0]
            for i in range(1, 10):
                if temp[i] > 1:
                    for j in range(9):
                        errors.append(row*9+j)
                    break
            temp = [0]*10
        for column in range(9):
            #Tarkistaa sarakkeet
            for i in range(9):
                temp[board_string[column+9*i]] += 1
            zeros += temp[0]
            for i in range(1, 10):
                if temp[i] > 1:
                    for j in range(9):
                        errors.append(column+j*9)
                    break
            temp = [0]*10
        for square in range(9):
            #Tarkistaa 3x3 ruudut
            for i in range(9):                
                temp[board_string[math.floor(square/3)*27+(square % 3)*3 +
                     math.floor(i/3)*9+i % 3]] += 1
            zeros += temp[0]
            for i in range(1, 10):
                if temp[i] > 1:
                    for j in range(9):
                        errors.append(math.floor(square/3)*27+(square % 3)*3 +
                                    math.floor(j/3)*9+j % 3)
                    break
            temp = [0]*10

        if len(errors) > 0:
            return errors
        if zeros == 0:
            return 2
        return 1
