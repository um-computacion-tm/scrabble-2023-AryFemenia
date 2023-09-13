#dibujar celdas del tablero
#calcular valor palabra
#FALTA: calcular puntaje segun multiplicador de palabra
from game.cell import Cell
from game.bagtiles import Tile

class Board:
    def __init__(self):
        self.grid = [[Cell(1, '') for _ in range(15)] for _ in range(15)]

    def calculate_word_value(self, word):
        value = 0
        for cell in word:
            value += cell.calculate_value()
        for cell in word:
            if cell.multiplier_type == 'word':
                value *= cell.multiplier
                cell.multiplier = 1
        return value

    def word_in_of_boad(self, word, location, orientation):
        if orientation == "H":
            return len(word) <= len(self.grid) - location[0]
        else:
            return len(word) <= len(self.grid) - location[1]

    def word_out_of_board(self, word, location, orientation):
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

    def validate_len_of_word(self, word):
        if len(word) > 7:
            return False
