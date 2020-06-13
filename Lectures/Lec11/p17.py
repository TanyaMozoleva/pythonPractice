'''
Complete the get_random_horoscope() function which returns
a random message. The function has 4 chances in 10 of returning
"Amazing day ahead", 3 chances in 10 of returning "Romance is very
likely", 1 chance in 10 of returning "Proceed with caution" and 2
chances in 10 of returning "Lucky lucky you".
'''

import random

def get_random_horoscope():
    message1 = 'Amazing day ahead'
    message2 = 'Romance is very likely'
    message3 = 'Proceed with caution'
    message4 = 'Lucky lucky you'
   
    message = ''
    number = random.randrange(10)
    if number < 4:
        message = message1
    elif number < 7:
        message = message2
    elif number < 9:
        message = message4
    else:
        message = message3
    return message

def main():
    print('Today\'s message: ', get_random_horoscope(), sep='')
    print('Today\'s message: ', get_random_horoscope(), sep='')

main()
