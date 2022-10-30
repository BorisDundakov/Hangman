class Word:

    def __init__(self, word):
        super().__init__()
        self.word = word
        self.occurrences = []

    @property
    def word(self):
        return self.__word

    @word.setter
    def word(self, value):
        if len(value) < 4:
            raise ValueError("Word is not of a valid size!")
        self.__word = value

    def display_initial(self):
        res = ''
        for letter in range(len(self.word)):
            if letter == 0:
                res += f'{self.word[letter]}'
            if letter == len(self.word) - 1:
                res += f'{self.word[letter]}'
            else:
                res += '_'
        print(res)

    def make_guess(self, letter):
        new_letter = [i for i, l in enumerate(self.word) if l == letter]
        if not new_letter:
            return False
        self.occurrences.extend(new_letter)
        if self.occurrences:
            res = self.correct_move(self.occurrences)
            return res

    def correct_move(self, known_idxs):
        result = ''
        for current_letter in range(len(self.word)):
            if current_letter == 0:
                result += self.word[current_letter]
            elif current_letter in list(known_idxs):
                result += f'{self.word[current_letter]}'
            elif current_letter == len(self.word):
                result += current_letter
            elif current_letter == len(self.word) - 1:
                result += f'{self.word[current_letter]}'
            else:
                result += '_'

        return result
