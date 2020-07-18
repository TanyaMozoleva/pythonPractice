'''
Complete the code in the main() function which changes
each string element of the list into an integer.
'''

import random
def main():
    a_list = ["6", "7", "5", "3", "8", "1", "9", "2", "8"]
    print("1.", a_list)

    for index in range(len(a_list)):
        a_list[index] = int(a_list[index])
    print("2.", a_list)

main()
