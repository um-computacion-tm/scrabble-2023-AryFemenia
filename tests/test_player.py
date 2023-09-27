import unittest
from game.player import Player
from game.bagtiles import *

class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player = Player("Ary", 0)

    def test_player_take_tiles(self):
        self.player.player_take_tiles(["A", "B", "C"])
        self.assertEqual(self.player.slug, ["A", "B", "C"])

    def test_player_return_tiles(self):
        self.player.player_take_tiles(["A", "B", "C"])
        self.player.player_return_tiles("B")
        self.assertEqual(self.player.slug, ["A", "C"])

    def test_validate_user_has_letters(self):
        bag_tile = TileBag()
        bag_tile.tiles = [
            Tile('H', 4),
            Tile('O', 1),
            Tile('L', 1),
            Tile('A', 1),
            Tile('B', 3),
            Tile('C', 3),
            Tile('I', 1),
        ]
        player = Player(bag_tile)
        tiles = [
            Tile('H', 1),
            Tile('O', 1),
            Tile('L', 1),
            Tile('A', 1),
        ]
        is_valid = player.has_letters(tiles)
        self.assertEqual(is_valid, True)

    def test_validate_user_has_letters(self):
        bag_tile = TileBag()
        bag_tile.tiles = [
            Tile('J', 4),
            Tile('O', 1),
            Tile('L', 1),
            Tile('A', 1),
            Tile('B', 3),
            Tile('C', 3),
            Tile('I', 1),
        ]
        player = Player(bag_tile)
        tiles = [
            Tile('H', 1),
            Tile('O', 1),
            Tile('L', 1),
            Tile('A', 1),
        ]
        is_valid = player.has_letters(tiles)
        self.assertEqual(is_valid, False)
    
if __name__ == '__main__':
    unittest.main()
