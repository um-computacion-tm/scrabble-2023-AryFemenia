#dibujar celdas del tablero
#calcular valor palabra
#FALTA: calcular puntaje segun multiplicador de palabra
from game.cell import Cell
from game.bagtiles import Tile

class Board:
    def __init__(self):
        self.grid = [[None for _ in range(15)] for _ in range(15)]

    def is_empty(self):
        for row in self.grid:
            for tile in row:
                if tile is not None:
                    return False
        return True
    
    @staticmethod
    def calculate_word_value(word: list[Cell]) -> int:
        value: int = 0
        multiplier_word = None
        for cell in word:
            value += cell.calculate_value()
            if cell.multiplier_type == 'word' and cell.active:
                multiplier_word = cell.multiplier
        if multiplier_word:
            value *= multiplier_word
        return value

    def validate_word_inside_board(self, word, location, orientation):
        row, col = location
        if orientation == "H":
            if col + len(word) <= len(self.grid) and row < len(self.grid):
                return True
        else:
            if row + len(word) <= len(self.grid) and col < len(self.grid):
                return True
        return False

    def validate_word_out_of_board(self, word, location, orientation):
        if orientation == "H":
            if len(word) > len(self.grid) - location[0]:
                return False 
            for i in range(len(word)):
                if self.grid[location[0] + i][location[1]].value != '':
                    return False 
        else: 
            if len(word) > len(self.grid) - location[1]:
                return False 
            for i in range(len(word)):
                if self.grid[location[0]][location[1] + i].value != '':
                    return False
        return True

    #WIP
    # def validate_len_of_word(self, word):
    #     if len(word) > 7:
    #         return False
