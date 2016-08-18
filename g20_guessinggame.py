'''Have the computer think of an integer between 1-100.

Have a human guess the number, responding higher/lower for incorrect guesses.

Bonus points: Keep a high-score table with names that persists between runs.
'''

import random


def guessing_game():
    print('Welcome to the guessing game')
    answer = int(random.random() * 100)

    while True:
        try:
            guess = int(raw_input('Guess: '))

        except ValueError:
            print('Not an int, try again')
            continue

        if guess == answer:
            print('You win!')
            return

        print('Higher' if guess < answer else 'Lower')


if __name__ == '__main__':
    guessing_game()
