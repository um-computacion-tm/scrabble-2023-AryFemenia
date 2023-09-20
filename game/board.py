#dibujar celdas del tablero
#calcular valor palabra
#FALTA: calcular puntaje segun multiplicador de palabra
from game.cell import Cell
from game.bagtiles import Tile

class Board:
    def __init__(self):
        self.grid = [[Cell(1, '') for _ in range(15)] for _ in range(15)]

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

    def is_empty(self):
        for row in self.grid:
            for cell in row:
                if cell.letter != '':
                    return False
        return True

    def validate_word_inside_board(self, word, location, orientation):
        row, col = location
        word_len = len(word)
        
        if orientation == "H":
            if col + word_len <= len(self.grid[0]) and 0 <= row < len(self.grid):
                for i in range(word_len):
                    if self.grid[row][col + i].letter != '':
                        return False
                return True
        else:
            if row + word_len <= len(self.grid) and 0 <= col < len(self.grid[0]):
                for i in range(word_len):
                    if self.grid[row + i][col].letter != '':
                        return False
                return True
        return False



    #WIP
    # def validate_len_of_word(self, word):
    #     if len(word) > 7:
    #         return False
