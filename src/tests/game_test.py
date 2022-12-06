import unittest

from sudoku.game import Game
from sudoku.board import Board
class TestGame(unittest.TestCase):
    def setUp(self):
        test_string = "000005309000270040100904020700000402000006100002050070031007960005000001900000000"
        board = Board(test_string)
        self.game = Game(board)

    def test_check_board_gives_no_faults_if_no_faults(self):
        self.assertEqual(self.game.check_board(),1)

    def test_check_board_returns_win_on_complete_board(self):
        won_string = "846253917129768453375941682517492836684315729293876145762584391958137264431629578"
        won_board = Board(won_string)
        self.assertEqual(Game(won_board).check_board(),2)

    def test_check_board_returns_faulty_row(self):
        self.game.board.change_value(0, 5)
        self.assertEqual(self.game.check_board(), [0, 1, 2, 3, 4, 5, 6, 7, 8])

    def test_check_board_returns_faulty_column(self):
        self.game.board.change_value(0, 7)
        self.assertEqual(self.game.check_board(), [0, 9, 18, 27, 36, 45, 54, 63, 72])

    def test_checkboard_returns_faulty_square(self):
        self.game.board.change_value(3, 4)
        self.assertEqual(self.game.check_board(), [3, 4, 5, 12, 13, 14, 21, 22, 23])