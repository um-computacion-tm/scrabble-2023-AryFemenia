import unittest
from game.board import Board


class TestBoard(unittest.TestCase):
    def test_init(self):
        cols = 15
        rows = 15
        board = Board(cols, rows)

        self.assertEqual(board.cols, cols)
        self.assertEqual(board.rows, rows)
    
    def place_word(self):
        pass

    def display(self):
        pass


if __name__ == '__main__':
    unittest.main()
