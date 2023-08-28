import unittest
from game.scrabble import ScrabbleGame


class TestScrabbleGame(unittest.TestCase):
    def test_init(self):
        game = ScrabbleGame(players_count=2)
        self.assertIsNotNone(game.board)
        self.assertEqual(len(game.players), 2)
        self.assertIsNotNone(game.bag_tiles)
        self.assertIsNotNone(game.dictionary)
    def test_init(self):
        game = ScrabbleGame(players_count=3)
        self.assertIsNotNone(game.board)
        self.assertEqual(len(game.players), 3)
        self.assertIsNotNone(game.bag_tiles)
        self.assertIsNotNone(game.dictionary)
    def test_init(self):
        game = ScrabbleGame(players_count=4)
        self.assertIsNotNone(game.board)
        self.assertEqual(len(game.players), 4)
        self.assertIsNotNone(game.bag_tiles)
        self.assertIsNotNone(game.dictionary)
    def test_start_method(self):
        pass   
    def test_play_method(self):
        pass


if __name__ == '__main__':
    unittest.main()
