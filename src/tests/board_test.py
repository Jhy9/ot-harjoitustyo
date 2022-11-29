import unittest

from sudoku.board import Board

class TestBoard(unittest.TestCase):
    def setUp(self):
        test_string = "000005309000270040100904020700000402000006100002050070031007960005000001900000000"
        self.board= Board(test_string)

    def test_str_unchanged_board_gives_test_string(self):
        self.assertEqual("000005309000270040100904020700000402000006100002050070031007960005000001900000000",str(self.board))
    
    def test_tile_value_can_be_changed(self):
        self.board.change_value(0,9)
        self.assertEqual("900005309000270040100904020700000402000006100002050070031007960005000001900000000",str(self.board))
