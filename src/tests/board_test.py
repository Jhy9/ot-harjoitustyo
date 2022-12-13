import unittest

from sudoku.board import Board
from sudoku.save_manager import SaveManager
class TestBoard(unittest.TestCase):
    def setUp(self):
        self.test_string = "000005309000270040100904020700000402000006100002050070031007960005000001900000000"
        self.board= Board(self.test_string)

    def test_str_unchanged_board_gives_test_string(self):
        self.assertEqual(self.test_string,str(self.board))
    
    def test_tile_value_can_be_changed(self):
        self.board.change_value(0,9)
        self.assertEqual(9, self.board.board[0].value)

    def test_inserting_invalid_value_doesnt_change_board(self):
        b = self.board
        self.board.change_value(0, -100)
        self.assertEqual(b, self.board)
