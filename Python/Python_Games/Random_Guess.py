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
    print(f'I am guessing a number between {low} & {high}')
    response = ''
    while response != 'y':
        guess = random.randint(low,high)
        
        response = str(input(f"Is the number \'{guess}\' yes(y), too high(h), or too low(l)?"))
        response = response.lower()

        if response == 'y' or response == 'yes':
            print('Yay! Awesome! Thanks for playing :)')
            break
        if response == 'l' or response == 'low':
            low = guess
            print(f'{low}')
        if response == 'h' or response == 'high':
            high = guess
            print(f'{high}')
        elif response == 'q' or response == 'quit':
            print('Until next time! Bye!')
            break
            
        
# player_guess(100)
computer_guess(50, 100)
