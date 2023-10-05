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

    def get_player_count():
        while True:
            try:
                player_count = int(input('cantidad de jugadores (1-3): '))
                if player_count <= 3:
                    break
            except Exception as e:
                print('ingrese un numero por favor')

        return player_count

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
