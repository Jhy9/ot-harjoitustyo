import unittest

from sudoku.tile import Tile


class TestTile(unittest.TestCase):
    def setUp(self):
        self.tile_static = Tile(5)
        self.tile_dynamic = Tile(0)

    def test_tile_static_is_locked(self):
        self.assertEqual(self.tile_static.lock, True)

    def test_tile_static_value_cannot_be_changed(self):
        self.tile_static.change_value(3)
        self.assertEqual(self.tile_static.value, 5)

    def test_tile_dynamic_is_unlocked(self):
        self.assertEqual(self.tile_dynamic.lock, False)

    def test_tile_dynamic_can_change_value(self):
        self.tile_dynamic.change_value(3)
        self.assertEqual(self.tile_dynamic.value, 3)

    def test_invalid_input_does_not_change_value(self):
        self.tile_dynamic.change_value(3)
        self.tile_dynamic.change_value("a")
        self.assertEqual(self.tile_dynamic.value, 3)

    def test_invalid_input_on_creation_sets_value_to_0(self):
        new_tile = Tile("a")
        self.assertEqual(new_tile.value, 0)

    def test_invalid_input_on_creation_does_not_lock_tile(self):
        new_tile = Tile("a")
        self.assertEqual(new_tile.lock, False)

    def test_tile_creation_does_not_lock_if_specified(self):
        new_tile = Tile(5, 0)
        self.assertEqual(new_tile.lock, False)