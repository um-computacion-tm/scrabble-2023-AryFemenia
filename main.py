#
from game.board import *

def main():
    print("Bienvenido")
    #players_count = input("Ingrese el numero de jugadores: ")

    player_count = get_player_count()
    game = ScrabbleGame(player_count)
    while game.is_playing():
        show_board(game.get_board())
        show_player(*game.get_current_player())
        word, coords, orientation = get_inputs()
        try:
            game.play(word, coords, orientation)
        except Exception as e:
            print(e)

    scrabble_board = Board()

    print("Tablero de Scrabble:")
    scrabble_board.__init__()

    def start_game():
        pass
    
    def validate_word(self, ):
        pass

    def get_words():
        pass

    def put_words():
        pass

if __name__ == '__main__':
    main()
