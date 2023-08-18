
import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        try:
            guess = int(input(f'Guess a number between 1 and {x}: '))
        except ValueError:
            print('Please enter an integer')
            continue
        else:
            if guess not in range(1, x+1):
                print('Please enter a number ONLY between 1 and 10')
                continue
            elif guess < random_number:
                print('Too low, guess again.')
            elif guess > random_number:
                print('Too high, guess again.')
            else:
                return print(f'Congratulations! You have guessed correctly! The number is {guess}.') 
   

guess(10)

