#
from game.bagtiles import TileBag

class Player:
    def __init__(self, name, points):
        self.name = name
        self.points = points
        self.slug = []

    def player_take_tiles(self, tile_bag, count):
        tiles = tile_bag.take(count)
        self.slug.extend(tiles)

    def player_return_tiles(self, tiles):
        self.slug.remove(tiles)

    def has_letters(self, tiles):
        for tile in tiles:
            if tile not in self.slug:
                return False
            else:
                self.player_return_tiles(tile)
        return True
