from View.display import Display


class Word(Display):

    def __init__(self, word):
        super().__init__()
        self.word = word
        self.occurances = []

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
        self.occurances.extend(new_letter)
        if self.occurances:
            res = self.correct_move(self.occurances)
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
