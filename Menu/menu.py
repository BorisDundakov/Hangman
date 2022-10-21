from Game.easy_game import EasyGame
from Game.medium_game import MediumGame
from Game.hard_game import HardGame


class Menu:
    def __init__(self):
        self.game_types = {1: EasyGame(), 2: MediumGame(), 3: HardGame()}

    def choose_game_type(self):
        print('Choose difficulty:')

        for number, g_type in self.game_types.items():
            print(f'{number} - {g_type.GAME_TYPE}')

        game_num = int(input('Please enter a digit: '))

        return self.game_types[game_num]
