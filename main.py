import random
import sys
import time
from concurrent.futures.thread import ThreadPoolExecutor
from multiprocessing import Process

from Menu.menu import Menu
from Word.word import Word
from View import messages


def game_logic(game, word):
    previous_guess = ''
    sys.stdin = open(0)
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
                return messages.winner

    print(messages.actual_word(word))
    print(messages.loser)


if __name__ == "__main__":
    menu = Menu()
    game = menu.choose_game_type()

    database = open("DemoDB/wordsDB.txt", "r")
    data = database.read()
    format_DB = data.split("\n")
    guess_word = ('two')
    # guess_word = (random.choice(format_DB))
    database.close()

    word = Word(guess_word)

    word.display_initial()
    # TODO: Two functions --> if one ends, the whole program ends

    # game logic > timer except for when the timer is up!
    if game.GAME_TYPE == 'hard':
        with ThreadPoolExecutor(max_workers=10) as executor:
            timer = executor.submit(game.run_timer)
            w = executor.submit(game_logic, game, word)

    else:
        result = game_logic(game, word)

    exit()
