#
from models import TileBag

class Player:
    def __init__(self, name, points):
        self.name = name
        self.points = points
        self.slug = []

    def player_take_tiles(self, tiles[]):
        self.slug.extend(tiles)
