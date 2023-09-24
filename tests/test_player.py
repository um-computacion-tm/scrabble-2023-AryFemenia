import unittest
from game.player import Player

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

if __name__ == '__main__':
    unittest.main()
