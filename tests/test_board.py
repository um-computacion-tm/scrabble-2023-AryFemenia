import unittest
from game.board import Board
from game.bagtiles import Tile

class TestBoard(unittest.TestCase):
    #1setup de board con tamaño correcto
    def test_init(self):
        board = Board()
        self.assertEqual(
            len(board.grid),
            15,
        )
        self.assertEqual(
            len(board.grid[0]),
            15,
        )
    #2si el board esta vacio o no(para verificar donde va a ir la primer palabra)
    def test_board_is_empty(self):
        board = Board()
        board.is_empty() == True
    
    def test_board_is_not_empty(self):
        board = Board()
        board.grid[7][7].add_letter(Tile("A", 1))
        assert board.is_empty() == False
    #3con el board NO vacio que la palabra este dentro del board
    def test_word_inside_board(self):
        board = Board()
        word = "Facultad"
        location = (5, 4)
        orientation = "H"

        word_is_valid = board.validate_word_inside_board(word, location, orientation)

        word_is_valid == True
    
    def test_word_out_of_board(self):
        board = Board()
        word = "Facultad"
        location = (14, 4)
        orientation = "H"

        word_is_valid = board.validate_word_inside_board(word, location, orientation)

        assert word_is_valid == False
    #4teniendo el board vacio, que la palabra se pueda poner en el board(vert u horiz)
    def test_place_word_empty_board_horizontal_fine(self):
        board = Board()
        word = "Facultad"
        location = (7, 4)
        orientation = "H"
        word_is_valid = board.validate_word_place_board(word, location, orientation)
        assert word_is_valid == True

    def test_place_word_empty_board_horizontal_wrong(self):
        board = Board()
        word = "Facultad"
        location = (2, 4)
        orientation = "H"
        word_is_valid = board.validate_word_place_board(word, location, orientation)
        word_is_valid == False

    def test_place_word_empty_board_vertical_fine(self):
        board = Board()
        word = "Facultad"
        location = (4, 7)
        orientation = "V"
        word_is_valid = board.validate_word_place_board(word, location, orientation)
        assert word_is_valid == True

    def test_place_word_empty_board_vertical_wrong(self):
        board = Board()
        word = "Facultad"
        location = (2, 4)
        orientation = "V"
        word_is_valid = board.validate_word_place_board(word, location, orientation)
        word_is_valid == False
    #5teniendo el board NO vacio, que la palabra se pueda poner en el board(vert u horiz)
    def test_place_word_not_empty_board_horizontal_fine(self):
        board = Board()
        board.grid[7][7].add_letter(Tile('C', 1))
        board.grid[8][7].add_letter(Tile('A', 1)) 
        board.grid[9][7].add_letter(Tile('S', 1)) 
        board.grid[10][7].add_letter(Tile('A', 1)) 
        word = "Facultad"
        location = (8, 6)
        orientation = "H"
        word_is_valid = board.validate_word_place_board(word, location, orientation)
        assert word_is_valid == True

    def test_calculate_word_value(self):
        pass

    def test_show_board(self):
        board = Board()
        board.show_board()

    def test_show_board_with_word(self):
        board = Board()
        board.grid[7][7].letter = Tile('h',4)
        board.grid[7][8].letter = Tile('o',1)
        board.grid[7][9].letter = Tile('l',1)
        board.grid[7][10].letter = Tile('a',1)

    def test_show_board_with_words(self):

        board = Board()
        board.grid[7][7].letter = Tile('h',4)
        board.grid[7][8].letter = Tile('o',1)
        board.grid[7][9].letter = Tile('l',1)
        board.grid[7][10].letter = Tile('a',1)

        board = Board()
        board.grid[7][7].letter = Tile('h',4)
        board.grid[8][7].letter = Tile('o',1)
        board.grid[9][7].letter = Tile('l',1)
        board.grid[10][7].letter = Tile('a',1)

'''   
    # validar  que la palabra se pueda poner en el board(vert u horiz)
    # def place_word_horizontal(self):
    #     word = [(1, 'A'), (2, 'B'), (1, 'C')]
    #     location = (0, 0)
    #     orientation = "H"

    #     for i, cell in enumerate(word):
    #         if orientation == "H":
    #             self.assertEqual(self.board.grid[location[0] + i][location[1]].value, cell.value)
    #         else:
    #             self.assertEqual(self.board.grid[location[0]][location[1] + i].value, cell.value)

    # def place_word_vertical(self):
    #     word = [Cell(1, 'A'), Cell(2, 'B'), Cell(1, 'C')]
    #     location = (0, 0)
    #     orientation = "V"

    #     for i, cell in enumerate(word):
    #         if orientation == "V":
    #             self.assertEqual(self.board.grid[location[0] + i][location[1]].value, cell.value)
    #         else:
    #             self.assertEqual(self.board.grid[location[0]][location[1] + i].value, cell.value)
'''
if __name__ == '__main__':
    unittest.main()
