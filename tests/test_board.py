import unittest
from game.board import Board
from game.cell import Cell

class TestBoard(unittest.TestCase):
    def test_init(self):
        self.board = Board()

    def place_word(self):
        word = [Cell(1, 'A'), Cell(2, 'B'), Cell(1, 'C')]
        location = (0, 0)
        orientation = "H"

        for i, cell in enumerate(word):
            if orientation == "H":
                self.assertEqual(self.board.grid[location[0] + i][location[1]].value, cell.value)
            else:
                self.assertEqual(self.board.grid[location[0]][location[1] + i].value, cell.value)

    def display(self):
        pass


if __name__ == '__main__':
    unittest.main()
