from Game.game import Game


class HardGame(Game):
    N_LIVES = 8
    GAME_TYPE = 'hard'

    def __init__(self):
        self.timer = None
        super().__init__(HardGame.GAME_TYPE, HardGame.N_LIVES)

    def add_timer(self, seconds):
        self.timer = seconds



