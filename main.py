import random
import sys
from multiprocessing import Process

from Menu.menu import Menu
from Word.word import Word
from View import messages


def game_logic(game, word):
    previous_guess = ''
    sys.stdin = open(0)
    while game.N_LIVES > 0:
        print('\r', messages.letter_guess, end=' ')
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
                return messages.winner

    print(messages.actual_word(word))
    return messages.loser


if __name__ == "__main__":
    menu = Menu()
    game = menu.choose_game_type()

    database = open("DemoDB/wordsDB.txt", "r")
    data = database.read()
    format_DB = data.split("\n")
    guess_word = (random.choice(format_DB))
    database.close()

    word = Word(guess_word)
    word.display_initial()

    if game.GAME_TYPE == 'hard':
        print(messages.timer_length)
        p1 = Process(target=game.run_timer)
        p2 = Process(target=game_logic, args=(game, word))
        p1.start()
        p2.start()
        while p1.is_alive():
            if not p2.is_alive():
                # 'successful guess or too many guesses!'
                p1.terminate()
                exit()

        else:
            print(messages.time_up)
            print(messages.actual_word(word))
            p2.terminate()
            exit()

    print(game_logic(game, word))

