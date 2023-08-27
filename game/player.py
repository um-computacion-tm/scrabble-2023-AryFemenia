from models import TileBag

class Player:
    def __init__(self):
        self.tiles = []

    def player_take_tiles(tile_bag, count):
        if count > 0:
            return tile_bag.take(count)
        else:
            return []

    tile_bag = TileBag()

    tiles_taken = player_take_tiles(tile_bag, 7)

    for tile in tiles_taken:
        print(f"Tile: {tile.letter}, Points: {tile.points}")

    print(f"Remaining tiles in the bag: {len(tile_bag.tiles)}")
