'''
The get_dice_throws_result() function throws a number of
dice (given by num_throws) and counts how often the dice value,
(given by dice_to_check) occurs. Complete the function.
'''

import random

def get_dice_throws_result(num_throws, dice_to_check):
    count = 0
    dices = 0
    while count < num_throws:
        if random.randrange(1,7) == dice_to_check:
            dices = dices + 1
        count = count + 1
    return dices 


def main():
    print('30000 throws,',  get_dice_throws_result(30000,  6), 'sixes')
    print('6 throws,',      get_dice_throws_result(6,      6), 'sixes')
    print('600000 throws,', get_dice_throws_result(600000, 5), 'fives')

main()
