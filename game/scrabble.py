#juntar board, player, models
#logica de siguiente jugador
from game.board import Board
from game.player import Player
from game.bagtiles import TileBag

class ScrabbleGame:
    def __init__(self, players_count: int):
        self.board = Board()
        self.bag_tiles = TileBag()
        self.players:list[Player] = []
        for _ in range(players_count):
            self.players.append(Player())
        self.current_player = None

    def play(self, word, location, orientation):
        self.validate_word(word, location, orientation)
        words = self.board.put_words(word, location, orientation)
        total = calculate_words_value(words)
        self.players[self.current_player].score += total
        self.next_turn()

    def next_turn(self):
        if self.current_player is None:
            self.current_player = self.players[0]
        else:
            self.current_player = self.players[self.players.index(self.current_player) + 1]

            # self.current_player_index = (self.current_player_index + 1) % len(self.players)
            # self.current_player = self.players[self.current_player_index]

    def validate_word(self, word, location, orientation):
        if not dict_validate_word(word):
            raise InvalidWordException("Su palabra no existe en el diccionario")
        if not self.board.validate_word_inside_board(word, location, orientation):
            raise InvalidPlaceWordException("Su palabra excede el tablero")
        if not self.board.validate_word_place_board(word, location, orientation):
            raise InvalidPlaceWordException("Su palabra esta mal puesta en el tablero")
        