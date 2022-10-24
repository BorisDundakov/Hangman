import os
import sys

from Game.game import Game
import time


class HardGame(Game):
    N_LIVES = 8
    GAME_TYPE = 'hard'

    def __init__(self):
        self.timer = 13
        super().__init__(HardGame.GAME_TYPE, HardGame.N_LIVES)

    def run_timer(self):
        while self.timer:
            mins, secs = divmod(self.timer, 60)
            timer = '{:02d}:{:02d}'.format(mins, secs)
            print('\r', timer, end='')
            time.sleep(1)
            self.timer -= 1

        mins, secs = divmod(self.timer, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print('\r', timer)
        return False
