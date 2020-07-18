'''
Complete the following function which is passed a list of ints
as a parameter and returns a new list in which each element is
the squared value of the element in the original list.
'''

import random
def get_list_of_squares(a_list):
    new_list = []
    for element in a_list:
        new_list = new_list + [element * element]
    return new_list

def main():
    my_list = list()
    for count in range(10):
        my_list = my_list + [random.randrange(1, 10)]

    # print("1.", get_list_of_squares(my_list))
    # print("2.", my_list)

main()

print(list('hello'))
