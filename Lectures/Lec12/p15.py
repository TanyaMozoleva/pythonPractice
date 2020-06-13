'''
'''

import random

def user_number_guess(computer_num):
    prompt = 'Enter your guess (1 - 99): '
    num_guesses = 1
    number = 0
    user_number = int(input(prompt))

    
    while computer_num != user_number:
        if user_number > computer_num:
            print('Too high')
        elif user_number < computer_num:
            print('Too low')
        num_guesses = num_guesses + 1
        user_number = int(input(prompt))

    print("Correct! Number of guesses:", num_guesses)


def main():
    number_to_guess = random.randrange(1,100)
    user_number_guess(number_to_guess)

main()
