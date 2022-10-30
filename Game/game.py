class Game:

    def __init__(self, game_type, n_lives):
        self.game_type = game_type
        self.n_lives = n_lives

    @property
    def n_lives(self):
        return self.__n_lives

    @n_lives.setter
    def n_lives(self, number_of_lives):
        if number_of_lives < 0:
            raise ValueError("Lives cannot be a negative value!")
        self.__n_lives = number_of_lives

    @staticmethod
    def check_winner(word):
        if word.isalpha():
            return True
        return False

    def display_hangman(self, error_counter):
        pass
