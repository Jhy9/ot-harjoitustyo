import unittest

from sudoku.tile import Tile


class TestTile(unittest.TestCase):
    def setUp(self):
        self.tile_static = Tile(5)
        self.tile_dynamic = Tile(0)

    def test_tile_static_is_locked(self):
        self.assertEqual(self.tile_static.lock, True)

    def test_tile_static_value_cannot_be_changed(self):
        self.tile_static.changeValue(3)
        self.assertEqual(self.tile_static.value, 5)

    def test_tile_dynamic_is_unlocked(self):        
        self.assertEqual(self.tile_dynamic.lock, False)
        
    def test_tile_dynamic_can_change_value(self):
        self.tile_dynamic.changeValue(3)
        self.assertEqual(self.tile_dynamic.value, 3)


    
     
