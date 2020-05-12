'''
Complete the following program which prompts the user once for the total
of 4 dice throws, the programs calculates the sum of four random dice
throws, and outputs the four dice values and the difference between the
user guess and the dice throwing simulation sum (see example outputs):
'''

import random

prompt = 'Enter sum (4 dice): '
dice_sum = 0
the_dice = "("

dice1 = random.randrange(1, 7)
dice2 = random.randrange(1, 7)
dice3 = random.randrange(1, 7)
dice4 = random.randrange(1, 7)
dice_sum = dice1 + dice2 + dice3 + dice4
user_sum = int(input(prompt))
difference = abs(user_sum - dice_sum)
the_dice = (the_dice + str(dice1) + ' ' + str(dice2) + 
            ' ' + str(dice3) + ' ' + str(dice4) + ')')
                   
print('The dice: ', the_dice, sep='')
print('Your total: ', user_sum, 'dice total: ', dice_sum, sep='')
print('You are out by: ', difference, sep='')
