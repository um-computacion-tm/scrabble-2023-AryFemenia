#omit C+H instead of CH/2xL instead of LL/2xR instead of RR
import random

class Tile:
    def __init__(self, letter, value):
        self.letter = letter
        self.value = value

#Español 100 piezas(fuera de Norte America)
class TileBag:
    def __init__(self):
        self.tiles = {
            'A': {'value': 1, 'count': 12},
            'B': {'value': 3, 'count': 2},
            'C': {'value': 3, 'count': 4},
            'CH': {'value': 3, 'count': 4},
            'D': {'value': 2, 'count': 5},
            'E': {'value': 1, 'count': 12},
            'F': {'value': 4, 'count': 1},
            'G': {'value': 2, 'count': 2},
            'H': {'value': 4, 'count': 2},
            'I': {'value': 1, 'count': 6},
            'J': {'value': 8, 'count': 1},
            'L': {'value': 1, 'count': 4},
            'LL': {'value': 1, 'count': 4},
            'M': {'value': 3, 'count': 2},
            'N': {'value': 1, 'count': 5},
            'Ñ': {'value': 8, 'count': 1},
            'O': {'value': 1, 'count': 9},
            'P': {'value': 3, 'count': 2},
            'Q': {'value': 5, 'count': 1},
            'R': {'value': 1, 'count': 5},
            'RR': {'value': 1, 'count': 5},
            'S': {'value': 1, 'count': 6},
            'T': {'value': 1, 'count': 4},
            'U': {'value': 1, 'count': 5},
            'V': {'value': 4, 'count': 1},
            'X': {'value': 8, 'count': 1},
            'Y': {'value': 4, 'count': 1},
            'Z': {'value': 10, 'count': 1},
            '': {'value': 0, 'count': 2},
        }
        shuffled_keys = list(self.tiles.keys())
        random.shuffle(shuffled_keys)
        
        self.tiles = {key: self.tiles[key] for key in shuffled_keys}

    def take(self, count):
        tiles = []
        for _ in range(count):
            available_letters = [letter for letter in self.tiles if self.tiles[letter]['count'] > 0]
            if not available_letters:
                break
            selected_letter = random.choice(available_letters)
            tiles.append(selected_letter)
            self.tiles[selected_letter]['count'] -= 1
        return tiles
    
    def put(self, tiles):
        self.tiles.extend(tiles)
#player emulation
scrabble_game = TileBag()

player_tiles = scrabble_game.take(7)
print("Your tiles:", player_tiles)
