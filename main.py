import random
import sys
from multiprocessing import Process

from Menu.menu import Menu
from Word.word import Word
from View import messages


def game_logic(game, word):
    previous_guess = ''
    sys.stdin = open(0)
    wrong_guesses_counter = 0
    while game.N_LIVES > 0:
        print('\r', messages.letter_guess, end=' ')
        guess = word.make_guess((input()))

        if guess == False:
            game.N_LIVES -= 1
            wrong_guesses_counter += 1
            print(messages.false_guess)
            print(game.display_hangman(wrong_guesses_counter))
            if previous_guess == '':
                word.display_initial()
            else:
                print(previous_guess)
        else:

            print(guess)
            previous_guess = guess
            winner = game.check_winner(guess)
            if winner:
                if game.GAME_TYPE == 'hard':
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
        timer_process = Process(target=game.run_timer)
        guess_process = Process(target=game_logic, args=(game, word))
        timer_process.start()
        guess_process.start()
        while timer_process.is_alive():
            if not guess_process.is_alive():
                # 'successful guess or too many guesses!'
                timer_process.terminate()
                exit()

        else:
            print(messages.time_up)
            print(messages.actual_word(word))
            guess_process.terminate()
            exit()
    else:
        print(game_logic(game, word))
