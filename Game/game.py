class Game:

    def __init__(self, game_type, n_lives):
        self.game_type = game_type
        self.n_lives = n_lives

    @staticmethod
    def check_winner(word):
        if word.isalpha():
            return True
        return False

    def display_hangman(self, error_counter):
        pass
