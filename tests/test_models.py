import unittest
from game.models import (
    TileBag,
    Tile,
)
from unittest.mock import patch

class TestTiles(unittest.TestCase):
    def test_tile(self):
        tile = Tile('A', 1)
        self.assertEqual(tile.letter, 'A')
        self.assertEqual(tile.value, 1)

class TestTileBag(unittest.TestCase):
    @patch('random.shuffle')
    def test_bag_tiles(self, patch_shuffle):
        bag = TileBag()
        self.assertEqual(
            len(bag.tiles),
            7,
        )
        self.assertEqual(
            patch_shuffle.call_count,
            1,
        )
        self.assertEqual(
            patch_shuffle.call_args[0][0],
            bag.tiles,
        )

    def test_take(self):
        bag = TileBag()
        tiles = bag.take(2)
        self.assertEqual(
            len(bag.tiles),
            5,
        )
        self.assertEqual(
            len(tiles),
            2,
        )

    def test_put(self):
        bag = TileBag()
        put_tiles = [Tile('Z', 1), Tile('Y', 1)]
        bag.put(put_tiles)
        self.assertEqual(
            len(bag.tiles),
            7,
        )

if __name__ == '__main__':
    unittest.main()
