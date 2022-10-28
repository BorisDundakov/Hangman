import os
import sys

from Game.game import Game
import time
from View.Hangman import hangman_hard_game


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

    def display_hangman(self, error_counter):
        wrong_moves = {
            '1': hangman_hard_game.wrong_move_1,
            '2': hangman_hard_game.wrong_move_2,
            '3': hangman_hard_game.wrong_move_3,
            '4': hangman_hard_game.wrong_move_4,
            '5': hangman_hard_game.wrong_move_5,
            '6': hangman_hard_game.wrong_move_6,
            '7': hangman_hard_game.wrong_move_7,
            '8': hangman_hard_game.wrong_move_8,

        }
        var = wrong_moves[str(error_counter)]
        return var
