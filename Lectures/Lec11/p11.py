'''
Using nested if statements complete the compare_nums1()
function which is passed two integers and returns a string. The function
compares the first number to the second number and returns one of the
following three strings (i.e., the string which is applicable):
"equal to" OR "less than" OR "greater than"
'''

import random

def compare_nums1(num1, num2):
    message = ''

    if num1 == num2:
        message = 'equal to '
    else: 
        if num1 > num2:
            message = 'greater than '
        else: 
            message = 'less than '
    return message

def main():
    num1 = random.randrange(1, 100)
    num2 = random.randrange(1, 100)
    comparison = compare_nums1(num1, num2)
    print(num1, ' is ', comparison, num2, sep='')

main()


