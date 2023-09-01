from game.cell import Cell

class Board:
    def __init__(self):
        self.grid = [[Cell(1, '') for _ in range(15)] for _ in range(15)]

def calculate_word_value(self):
    value = 0
    for row in self.grid:
        for cell in row:
            value += cell.calculate_points_letter()
    return value

    

#tablero tiene los puntos de las palabras pero no es el q lo calcula(la celda es la que calcula)