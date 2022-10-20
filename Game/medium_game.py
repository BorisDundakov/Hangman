from Game.game import Game


class MediumGame(Game):
    N_LIVES = 20
    GAME_TYPE = 'medium'

    def __init__(self):
        super().__init__(MediumGame.GAME_TYPE, MediumGame.N_LIVES)
