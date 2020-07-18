'''
Complete the code in the main() function which adds 1 to
each list element in the list which has an odd value.
'''

import random
def main():
    a_list = []
    for index in range(10):
        a_list = a_list + [random.randrange(1, 100)]
    print("1.", a_list)

    for index in range(len(a_list)):
        if a_list[index] % 2 == 1:
            a_list[index]= a_list[index] + 1
    print("2.", a_list)

main()
