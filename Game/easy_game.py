from Game.game import Game
from View.Hangman import hangman_easy_game


class EasyGame(Game):
    N_LIVES = 22
    GAME_TYPE = 'easy'

    def __init__(self):
        super().__init__(EasyGame.GAME_TYPE, EasyGame.N_LIVES)

    def display_hangman(self, error_counter):
        wrong_moves = {
            '1': hangman_easy_game.wrong_move_1,
            '2': hangman_easy_game.wrong_move_2,
            '3': hangman_easy_game.wrong_move_3,
            '4': hangman_easy_game.wrong_move_4,
            '5': hangman_easy_game.wrong_move_5,
            '6': hangman_easy_game.wrong_move_6,
            '7': hangman_easy_game.wrong_move_7,
            '8': hangman_easy_game.wrong_move_8,
            '9': hangman_easy_game.wrong_move_9,
            '10': hangman_easy_game.wrong_move_10,
            '11': hangman_easy_game.wrong_move_11,
            '12': hangman_easy_game.wrong_move_12,
            '13': hangman_easy_game.wrong_move_13,
            '14': hangman_easy_game.wrong_move_14,
            '15': hangman_easy_game.wrong_move_15,
            '16': hangman_easy_game.wrong_move_16,
            '17': hangman_easy_game.wrong_move_17,
            '18': hangman_easy_game.wrong_move_18,
            '19': hangman_easy_game.wrong_move_19,
            '20': hangman_easy_game.wrong_move_20,
            '21': hangman_easy_game.wrong_move_21,
            '22': hangman_easy_game.wrong_move_22,

        }
        var = wrong_moves[str(error_counter)]
        return var
