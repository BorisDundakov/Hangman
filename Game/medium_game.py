from Game.game import Game
from View.Hangman import hangman_medium_game


class MediumGame(Game):
    N_LIVES = 14
    GAME_TYPE = 'medium'

    def __init__(self):
        super().__init__(MediumGame.GAME_TYPE, MediumGame.N_LIVES)

    def display_hangman(self, error_counter):
        wrong_moves = {
            '1': hangman_medium_game.wrong_move_1,
            '2': hangman_medium_game.wrong_move_2,
            '3': hangman_medium_game.wrong_move_3,
            '4': hangman_medium_game.wrong_move_4,
            '5': hangman_medium_game.wrong_move_5,
            '6': hangman_medium_game.wrong_move_6,
            '7': hangman_medium_game.wrong_move_7,
            '8': hangman_medium_game.wrong_move_8,
            '9': hangman_medium_game.wrong_move_9,
            '10': hangman_medium_game.wrong_move_10,
            '11': hangman_medium_game.wrong_move_11,
            '12': hangman_medium_game.wrong_move_12,
            '13': hangman_medium_game.wrong_move_13,
            '14': hangman_medium_game.wrong_move_14,

        }
        var = wrong_moves[str(error_counter)]
        return var
