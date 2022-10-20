from Game.game import Game


class EasyGame(Game):
    N_LIVES = 23
    GAME_TYPE = 'easy'

    def __init__(self):
        super().__init__(EasyGame.GAME_TYPE, EasyGame.N_LIVES)
