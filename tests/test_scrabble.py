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

    def test_next_turn_when_game_is_starting(self):
        #validadr que al comienzo, el turno es del jugador 0
        scrabble_game = ScrabbleGame(players_count=3)
        scrabble_game.next_turn()
        assert scrabble_game.current_player == scrabble_game.players[0]
    def test_next_turn_when_player_is_not_first(self):
        #validadr que al comienzo, el turno es del jugador 1
        scrabble_game = ScrabbleGame(players_count=3)
        scrabble_game.current_player == scrabble_game.players[0]
        scrabble_game.next_turn()
        assert scrabble_game.current_player == scrabble_game.players[1]
    def test_next_turn_when_player_is_last(self):
        #validadr que al comienzo, el turno es del jugador 2
        scrabble_game = ScrabbleGame(players_count=3)
        scrabble_game.current_player == scrabble_game.players[2]
        scrabble_game.next_turn()
        assert scrabble_game.current_player == scrabble_game.players[2]

if __name__ == '__main__':
    unittest.main()
