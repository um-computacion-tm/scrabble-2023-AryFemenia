import unittest
from game.scrabble import ScrabbleGame


class TestScrabbleGame(unittest.TestCase):
    def test_init(self):
        scrabble_game = ScrabbleGame(players_count=1)
        self.assertIsNotNone(scrabble_game.board)
        self.assertEqual(
            len(scrabble_game.players),
            1,
        )
        self.assertIsNotNone(scrabble_game.bag_tiles)
    def test_init(self):
        scrabble_game = ScrabbleGame(players_count=1)
        self.assertIsNotNone(scrabble_game.board)
        self.assertEqual(
            len(scrabble_game.players),
            1,
        )
        self.assertIsNotNone(scrabble_game.bag_tiles)
    def test_init(self):
        scrabble_game = ScrabbleGame(players_count=2)
        self.assertIsNotNone(scrabble_game.board)
        self.assertEqual(
            len(scrabble_game.players),
            2,
        )
        self.assertIsNotNone(scrabble_game.bag_tiles)
    def test_init(self):
        scrabble_game = ScrabbleGame(players_count=3)
        self.assertIsNotNone(scrabble_game.board)
        self.assertEqual(
            len(scrabble_game.players),
            3,
        )
        self.assertIsNotNone(scrabble_game.bag_tiles)
    def test_init(self):
        scrabble_game = ScrabbleGame(players_count=4)
        self.assertIsNotNone(scrabble_game.board)
        self.assertEqual(
            len(scrabble_game.players),
            4,
        )
        self.assertIsNotNone(scrabble_game.bag_tiles)


if __name__ == '__main__':
    unittest.main()
