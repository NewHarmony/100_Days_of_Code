#Number guessing game

import random

def guess(x):
    random_number = random.randint(1,x)
    guess = 0
    while guess != random_number:
        guess = (input(f'Guess a number between 1 and {x}: '))
        if guess.lower == 'q':
            print("Thanks for playing! Bye!")
        else:
            guess = int(guess)
            if guess < random_number:
                print('Sorry, too low. Guess again. Or press \'q\' to quit.')
            elif guess > random_number:
                print('Sorry, too high. Guess again. Or press \'q\' to quit.')
            elif guess == random_number:
                print(f'Congrats! You have guessed the correct number: {random_number}! ')

guess(100)