from View.display import Display


class Word(Display):

    def __init__(self, word):
        super().__init__()
        self.word = word

    def correct_move(self, letter_idx, *known_idxs):
        list(known_idxs).append(letter_idx)
        result = ''
        for current_letter in range(len(self.word)):
            if current_letter == 0:
                result += current_letter
            if current_letter in known_idxs:
                result += f'{self.word[current_letter]}'
            if current_letter == len(self.word):
                result += current_letter
            else:
                result += '_'
        return result
