'''
Complete the code in the main() function which changes
the elements starting from index 1 so that each element is
the accumulative total of the previous elements (i.e., element
1 is the sum of the element 0 and element 1, element 2 is the
sum of element 1 and element 2, etc.).
'''

import random
def main():
    a_list = []
    for num in range(10):
        a_list = a_list + [random.randrange(1, 10)]
    print("1.", a_list)

    for index in range(1, len(a_list)):
        a_list[index] = a_list[index] + a_list[index-1]

    print("2.", a_list)

main()
