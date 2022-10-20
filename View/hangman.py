"""
hangman.py
_____________
            |
            |
            |
         ________
        |       |
        |_______|
            |
            |
        ----|----
            |
            |
           | \
          |   \
         |     \

"""

from View.display import Display


class Hangman(Display):
    def __init__(self, game_type):
        super().__init__()
        self.game_type = game_type

    def wrong_move(self, counter):
        # print different results according to the different game_type
        pass




