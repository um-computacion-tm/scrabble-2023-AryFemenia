import unittest
from game.board import calculate_word_value
from game.cell import Cell
from game.bagtiles import Tile

class TestCalculateWordValue(unittest.TestCase):
    def test_simple(self):
        word = [
            Cell(letter='p', points=3),
            Cell(letter='a', points=1),
            Cell(letter='n', points=1),
        ]
        value = calculate_word_value(word)
        self.assertEqual(value, 5)
    
    def test_with_letter_multiplier(self):
        word = [
            Cell(
                letter=Tile('p', 3, 
                multiplier=2, 
                multiplier_type='letter'
                )),
            Cell(letter=Tile('a', 1)),
            Cell(letter=Tile('n', 1)),
        ]
        value = calculate_word_value(word)
        self.assertEqual(value, 8)

    def test_with_word_multiplier(self):
        word = [
            Cell(letter=Tile('p', 3)),
            Cell(letter=Tile('a', 1)),
            Cell(
                letter=Tile('n', 1, 
                multiplier=2, 
                multiplier_type='word'
                )),
        ]
        value = calculate_word_value(word)
        self.assertEqual(value, 10)

    def test_with_letter_word_multiplier(self):
        word = [
            Cell(
                letter=Tile('p', 3, 
                multiplier=2, 
                multiplier_type='letter'
                )),
            Cell(letter=Tile('a', 1)),
            Cell(
                letter=Tile('n', 1, 
                multiplier=2, 
                multiplier_type='word'
                )),
        ]
        value = calculate_word_value(word)
        self.assertEqual(value, 16)

    def test_with_letter_word_multiplier_no_active(self):
        # QUE HACEMOS CON EL ACTIVE ????
        word = [
            Cell(
                multiplier=3,
                multiplier_type='letter',
                letter=Tile('C', 1)
            ),
            Cell(letter=Tile('A', 1)),
            Cell(
                letter=Tile('S', 2),
                multiplier=2,
                multiplier_type='word',
            ),
            Cell(letter=Tile('A', 1)),
        ]
        value = calculate_word_value(word)
        self.assertEqual(value, 5)
    
if __name__ == '__main__':
    unittest.main()
