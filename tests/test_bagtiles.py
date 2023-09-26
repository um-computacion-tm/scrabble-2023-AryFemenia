import unittest
from game.bagtiles import (
    Tile,
    TileBag,
)
from unittest.mock import patch

class TestTilesPoints(unittest.TestCase):
    def test_tile(self):
        tile = Tile('A', 1)
        self.assertEqual(tile.letter, 'A')
        self.assertEqual(tile.points, 1)
    def test_tile(self):
        tile = Tile('E', 1)
        self.assertEqual(tile.letter, 'E')
        self.assertEqual(tile.points, 1)
    def test_tile(self):
        tile = Tile('I', 1)
        self.assertEqual(tile.letter, 'I')
        self.assertEqual(tile.points, 1)
    def test_tile(self):
        tile = Tile('L', 1)
        self.assertEqual(tile.letter, 'L')
        self.assertEqual(tile.points, 1)
    def test_tile(self):
        tile = Tile('N', 1)
        self.assertEqual(tile.letter, 'N')
        self.assertEqual(tile.points, 1)
    def test_tile(self):
        tile = Tile('O', 1)
        self.assertEqual(tile.letter, 'O')
        self.assertEqual(tile.points, 1)
    def test_tile(self):
        tile = Tile('R', 1)
        self.assertEqual(tile.letter, 'R')
        self.assertEqual(tile.points, 1)
    def test_tile(self):
        tile = Tile('S', 1)
        self.assertEqual(tile.letter, 'S')
        self.assertEqual(tile.points, 1)
    def test_tile(self):
        tile = Tile('T', 1)
        self.assertEqual(tile.letter, 'T')
        self.assertEqual(tile.points, 1)
    def test_tile(self):
        tile = Tile('U', 1)
        self.assertEqual(tile.letter, 'U')
        self.assertEqual(tile.points, 1)
    def test_tile(self):
        tile = Tile('D', 2)
        self.assertEqual(tile.letter, 'D')
        self.assertEqual(tile.points, 2)
    def test_tile(self):
        tile = Tile('G', 2)
        self.assertEqual(tile.letter, 'G')
        self.assertEqual(tile.points, 2)
    def test_tile(self):
        tile = Tile('B', 3)
        self.assertEqual(tile.letter, 'B')
        self.assertEqual(tile.points, 3)
    def test_tile(self):
        tile = Tile('C', 3)
        self.assertEqual(tile.letter, 'C')
        self.assertEqual(tile.points, 3)
    def test_tile(self):
        tile = Tile('M', 3)
        self.assertEqual(tile.letter, 'M')
        self.assertEqual(tile.points, 3)
    def test_tile(self):
        tile = Tile('P', 3)
        self.assertEqual(tile.letter, 'P')
        self.assertEqual(tile.points, 3)
    def test_tile(self):
        tile = Tile('F', 4)
        self.assertEqual(tile.letter, 'F')
        self.assertEqual(tile.points, 4)    
    def test_tile(self):
        tile = Tile('H', 4)
        self.assertEqual(tile.letter, 'H')
        self.assertEqual(tile.points, 4)
    def test_tile(self):
        tile = Tile('V', 4)
        self.assertEqual(tile.letter, 'V')
        self.assertEqual(tile.points, 4)
    def test_tile(self):
        tile = Tile('Y', 4)
        self.assertEqual(tile.letter, 'Y')
        self.assertEqual(tile.points, 4)
    def test_tile(self):
        tile = Tile('CH', 5)
        self.assertEqual(tile.letter, 'CH')
        self.assertEqual(tile.points, 5)
    def test_tile(self):
        tile = Tile('Q', 5)
        self.assertEqual(tile.letter, 'Q')
        self.assertEqual(tile.points, 5)    
    def test_tile(self):
        tile = Tile('J', 8)
        self.assertEqual(tile.letter, 'J')
        self.assertEqual(tile.points, 8)
    def test_tile(self):
        tile = Tile('LL', 8)
        self.assertEqual(tile.letter, 'LL')
        self.assertEqual(tile.points, 8)
    def test_tile(self):
        tile = Tile('Ñ', 8)
        self.assertEqual(tile.letter, 'Ñ')
        self.assertEqual(tile.points, 8)
    def test_tile(self):
        tile = Tile('RR', 8)
        self.assertEqual(tile.letter, 'RR')
        self.assertEqual(tile.points, 8)    
    def test_tile(self):
        tile = Tile('X', 8)
        self.assertEqual(tile.letter, 'X')
        self.assertEqual(tile.points, 8)
    def test_tile(self):
        tile = Tile('Z', 10)
        self.assertEqual(tile.letter, 'Z')
        self.assertEqual(tile.points, 10)
    def test_tile(self):
        tile = Tile('joker', 0)
        self.assertEqual(tile.letter, 'joker')
        self.assertEqual(tile.points, 0)

class TestTileBag(unittest.TestCase):
    @patch('random.shuffle')
    def test_bag_tiles(self, patch_shuffle):
        bag = TileBag()
        self.assertEqual(
            len(bag.tiles),
            98,
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
            96,
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
            100,
        )

if __name__ == '__main__':
    unittest.main()
