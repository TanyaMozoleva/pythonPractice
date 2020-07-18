'''
Using a for...in range() loop complete the print_series()
function which prints a series of numbers starting from the parameter
value, start_num. The second number printed is the first number
plus 1, the third number is the second number plus 2, the fourth
number is the third number plus 3, and so on, e.g., a series of 8
numbers starting from the number 2 is:
'''

def print_series(start_num, how_many):
    number = start_num # 2
    for value in range(0, how_many):
        number = number + value
        print(number, end=' ')
    print()




def main():
    print_series(2, 8)
    print_series(5, 12)
    print_series(16, 9)


main()
