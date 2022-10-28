from Game.game import Game
from View.Hangman import hangman_easy_game


class MediumGame(Game):
    N_LIVES = 18
    GAME_TYPE = 'medium'

    def __init__(self):
        super().__init__(MediumGame.GAME_TYPE, MediumGame.N_LIVES)
