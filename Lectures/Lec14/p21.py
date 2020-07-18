'''
Complete the print_xs() function which prints a line of
characters: an "X" is printed if the corresponding element of
the parameter list is True, otherwise a space is printed (see
the output of the example below where the elements in
indexes 0, 3 and 5 are True).

'''

def print_xs(a_list):
    for element in a_list:
        if element == True:
            print('X', end='')
        else:
            print(' ', end='')
    print()

def main():
    print("0123456789")
    my_list = [True, False, False, True, False, True]
    print_xs(my_list)


main()
