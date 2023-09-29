#dibujar celdas del tablero
#calcular valor palabra
#FALTA: calcular puntaje segun multiplicador de palabra
from game.cell import Cell
from game.bagtiles import Tile

class Board:
    def __init__(self):
        self.grid = [[Cell(1, '') for _ in range(15)] for _ in range(15)]

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
    
    def validate_word_place_board(self, word, location, orientation):
        row, col = location
        word_len = len(word)
        
        if orientation == "H":
            if col + word_len <= len(self.grid[0]) and 0 <= row < len(self.grid):
                for i in range(word_len):
                    self.grid[row][col + i].add_letter(Tile(word[i], 1))
                return True
        else:
            if row + word_len <= len(self.grid) and 0 <= col < len(self.grid[0]):
                for i in range(word_len):
                    self.grid[row + i][col].add_letter(Tile(word[i], 1))
                return True
        return False

    @staticmethod
    def calculate_word_value(word: list[Cell]) -> int:
        value: int = 0
        multiplier_word = None
        for cell in word:
            value += cell.calculate_points_letter()
            if cell.multiplier_type == 'word' and cell.active:
                multiplier_word = cell.multiplier
        if multiplier_word:
            value *= multiplier_word
        return value

    def show_board(self):
        print('')
        col = ['   ','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O']
        print("  ".join(col))
        print('    ','1','','2','','3','','4','','5','','6','','7','','8','','9','','10','11','12','13','14','15')
        row  = [' 1',' 2',' 3',' 4',' 5',' 6',' 7',' 8',' 9','10','11','12','13','14','15']
        for i in range(15):
            print(row[i], end='|  ')
            for j in range(15):
                if self.grid[i][j].letter is None:
                    print('-', end='  ')
                else:
                    print(self.grid[i][j].letter.letter.upper(), end='  ')
            print('')
        print('')
    
    #WIP
    # def validate_len_of_word(self, word):
    #     if len(word) > 7:
    #         return False
