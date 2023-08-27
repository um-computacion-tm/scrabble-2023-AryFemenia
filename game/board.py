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

scrabble_board = Board(15, 15)
# Colocar una palabra en el tablero en posición horizontal
scrabble_board.place_word("python", 7, 5, 'horizontal')

# Colocar otra palabra en el tablero en posición vertical
scrabble_board.place_word("code", 5, 8, 'vertical')

scrabble_board.display()