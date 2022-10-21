class Game:
    WINS = 0
    LOSSES = 0

    def __init__(self, game_type, n_lives):
        self.game_type = game_type
        self.n_lives = n_lives

    @staticmethod
    def check_winner(word):
        if word.isalpha():
            return True
        return False

    def get_class_name(self):
        return self.__class__.__name__
