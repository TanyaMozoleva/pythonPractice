'''
Using and if ... elif statement complete the compare_nums2()
function which is passed two integers and returns a string. The function
compares the first number to the second number and returns one of the
following three strings (i.e., the string which is applicable):
"equal to" OR "less than" OR "greater than"
'''

import random

def compare_nums2(num1, num2):
    message = ''
    if num1 == num2:
        message = 'equal to '
    elif num1 > num2:
        message = 'greater than '
    else:
        message = 'less than '
    return message

def main():
    num1 = random.randrange(1, 100)
    num2 = random.randrange(1, 100)
    comparison = compare_nums2(num1, num2)
    print(num1, ' is ', comparison, num2, sep='')
main()
