'''
Complete the print_message() function which has an equal
chance of printing "now", "soon" and "never". Example output from
the completed program is shown lower down:
'''

import random
def print_message():
    number = random.randrange(1,4)
    if number == 1:
        print('now')
    if number == 2:
        print('soon')
    if number == 3:
        print('never')


def main():
    print("Life will improve")
    print_message()

main()
