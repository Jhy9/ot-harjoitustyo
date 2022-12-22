import unittest

from sudoku.save_manager import SaveManager
from sudoku.board import Board

class TestSaveManager(unittest.TestCase):
    def setUp(self):
        self.test_string = "000005309000270040100904020700000402000006100002050070031007960005000001900000000"
        self.board= Board(self.test_string)
        self.save = SaveManager()

    def test_saving_and_loading_gives_same_board_numbers(self):
        self.save.save_game("src/Savegame/test",self.board)
        new_board = self.save.load_game("src/Savegame/test.txt")
        self.assertEqual(str(self.board), str(new_board))

    def test_saving_and_loading_gives_same_board_locks(self):
        self.save.save_game("src/Savegame/test",self.board)
        new_board = self.save.load_game("src/Savegame/test.txt")
        self.assertEqual(self.board.locks, new_board.locks)

    def test_saving_modified_game_keeps_changes(self):
        board_two = Board(self.test_string)
        board_two.change_value(1, 1)
        self.save.save_game("src/Savegame/test",board_two)
        new_board = self.save.load_game("src/Savegame/test.txt")
        self.assertNotEqual(str(self.board), str(new_board))
    
    def test_saving_modified_game_keeps_locks(self):
        board_two = Board(self.test_string)
        board_two.change_value(1, 1)
        self.save.save_game("src/Savegame/test",board_two)
        new_board = self.save.load_game("src/Savegame/test.txt")
        self.assertEqual(self.board.locks, new_board.locks)