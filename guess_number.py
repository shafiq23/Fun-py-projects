import random
from sre_constants import GROUPREF
from webbrowser import Elinks

def guess(x):
    random_number = random.randint(1,x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a numbr between 1 and {x}: '))
        if guess < random_number:
            print('Guess again. Too low.')
        elif guess > random_number:
            print('Guess again, Too high.')
    print(f'Guessed the correct number, {random_number} correctly !!')

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = input(f'is {guess} too high (H), too low(L), or correct(C) ??').lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
    print(f'Guessed the correct number, {guess} correctly !!')

computer_guess(1000)

