from Menu.menu import Menu
from Word.word import Word
from View import messages

if __name__ == "__main__":
    menu = Menu()
    game = menu.choose_game_type()
    # TODO: word to be randomly selected from a postresql DB of words
    word = Word('forgotten')
    word.display_initial()
    previous_guess = ''
    while game.N_LIVES > 0:
        print(messages.letter_guess)

        guess = word.make_guess((input()))

        if guess == False:
            game.N_LIVES -= 1
            print(messages.false_guess)
            if previous_guess == '':
                word.display_initial()
            else:
                print(previous_guess)
        else:
            print(guess)
            previous_guess = guess
            winner = game.check_winner(guess)
            if winner:
                print(messages.winner)
                exit()

    print(messages.loser)
