'''
Complete the user_number_guess() function which keeps
prompting the user to guess a hidden number until the user correctly
guesses the number. At each guess the function lets the user know if
the guess is too high or too low. At the end, the function also prints the
number of guesses taken.
'''
import random

def user_number_guess(computer_num):
    prompt = 'Enter your guess (1 - 99): '
    num_guesses = 1
    number = 0 
    user_number = int(input(prompt))

    while computer_num != user_number:
        if user_number < computer_num:
            print('Too low')
        elif user_number > computer_num:
            print('Too high')
        num_guesses = num_guesses + 1
        user_number = int(input(prompt))

    print("Correct! Number of guesses:", num_guesses)

def main():
    user_number_guess(random.randrange(1, 100))

main()
