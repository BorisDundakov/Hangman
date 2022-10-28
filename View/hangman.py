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

    def wrong_move(self, instance, counter):
        counter += 1
        var_name = f'wrong_move{counter}'
        return instance.var_name

        # if self.game_type == 'hard':
        #     print(self.var_name)
        #     pass
        # elif self.game_type == 'medium':
        #     pass
        # elif self.game_type == 'easy':
        #     pass

        # # print different results according to the different game_type
