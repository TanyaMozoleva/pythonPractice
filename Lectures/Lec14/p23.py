'''
Complete the following function which prints the largest even
number in the parameter list. You can assume that there is at
least one element in the list. If the list contains no even numbers
message1 is printed.
'''

import random

def print_highest_even_num(a_list):
    message1 = "There are no even numbers in this list."
    message2 = "The highest even number: "
    max_even_number = 0

    for number in a_list:
        if number % 2 == 0 and number > max_even_number:
            max_even_number = number

    if max_even_number > 0:
        print(message2, max_even_number, sep='')
    else:
        print(message1)



def main():
    my_list = list()
    for count in range(0, 10):
        my_list = my_list + [random.randrange(10, 100)]

    print("1.", my_list)
    print_highest_even_num(my_list)
main()
