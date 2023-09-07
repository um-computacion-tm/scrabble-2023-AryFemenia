#añadir letra
#calcular puntaje
from game.models import Tile

class Cell:
    def __init__(self, multiplier=1, multiplier_type=''):
        self.multiplier = multiplier
        self.multiplier_type = multiplier_type
        self.letter = None

    def add_letter(self, letter:Tile):
        self.letter = letter

    def calculate_points_letter(self):
        if self.letter is None:
            return 0
        if self.multiplier_type == 'letter':
            return self.letter.points * self.multiplier
        else:
            return self.letter.points
