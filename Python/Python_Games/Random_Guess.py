#Number guessing game

import random

def player_guess(x):
    random_number = random.randint(1,x)
    guess = 0
    while guess != random_number:
        guess = (input(f'Guess a number between 1 and {x}: '))
        if str(guess)== 'q':
            print("Thanks for playing! Bye!")
            break

        else:
            guess = int(guess)
            if guess < random_number:
                print('Sorry, too low. Guess again. Or press \'q\' to quit.')
            elif guess > random_number:
                print('Sorry, too high. Guess again. Or press \'q\' to quit.')
            elif guess == random_number:
                print(f'Congrats! You have guessed the correct number: {random_number}! ')

def computer_guess(low, high):
    while response != 'y':

        guess = random.randint(low,high)
        response = str(input(f"Is the number \'{guess}\' yes(y), high(h), or low(l)?"))
        response = response.lower
        if response == 'y'|| response == 'yes':
            print(f'Awesome! Thanks for playing :)')
        if response == 'l'|| response == 'low':
            low = guess
            guess = random.randint(low,high)
        elif response == 'h'|| response == 'high':
            high = guess
            guess = random.randint(low,high)
        


player_guess(100)
