import os
import sys

from Game.game import Game
import time


class HardGame(Game):
    N_LIVES = 8
    GAME_TYPE = 'hard'

    def __init__(self):
        self.timer = 60
        super().__init__(HardGame.GAME_TYPE, HardGame.N_LIVES)

    def run_timer(self):
        while self.timer:
            time.sleep(1)
            self.timer -= 1

        return None
