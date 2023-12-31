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

    def next_turn(self):
        if self.current_player is None:
            self.current_player = self.players[0]
        else:
            self.current_player = self.players[self.players.index(self.current_player) + 1]

            # self.current_player_index = (self.current_player_index + 1) % len(self.players)
            # self.current_player = self.players[self.current_player_index]