from game.board import Board
from game.player import Player
from game.models import TileBag

class ScrabbleGame:
    def __init__(self, players_count):
        self.board = Board()
        self.players = []
        self.bag_tiles = TileBag()
        for _ in range(players_count):
            self.players.append(Player())

    # def start(self):
    #     for player in self.players:
    #         player.draw_tiles(self.bag_tiles)
    #     self.board.display()
    #     self.play()
    
    # def play(self):
    #     while True:
    #         for player in self.players:
    #             player.play_turn(self.board, self.bag_tiles, self.dictionary)
    #             self.board.display()
    #             if self.bag_tiles.is_empty():
    #                 print("Game over!")
    #                 return
