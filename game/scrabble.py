from game.board import Board
from game.player import Player
from game.models import TileBag
from game.dictionary import Dictionary

class ScrabbleGame:
    def __init__(self, players_count):
        self.board = Board()
        self.players = []
        self.bag_tiles = TileBag()        
        self.dictionary = Dictionary()
        for _ in range(players_count):
            self.players.append(Player())
