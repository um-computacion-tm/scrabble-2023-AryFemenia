from game.cell import Cell

class Board:
    def __init__(self, cols, rows):
        self.cols = cols
        self.rows = rows
        self.grid = [
            [' ' for _ in range(cols)] 
            for _ in range(rows)
        ]

    def place_word(self, word, row, col, direction):
        if direction == 'horizontal':
            for i, letter in enumerate(word):
                self.grid[row][col + i] = letter
        elif direction == 'vertical':
            for i, letter in enumerate(word):
                self.grid[row + i][col] = letter

    def display(self):
        for row in self.grid:
            print(' '.join(row))
            print('-' * (self.cols * 2 - 1))
