'''
'''


def print_even_numbers(first_num, last_num):
    if last_num < first_num:
        return 
    number = first_num
    
    while number <= last_num:
        if number % 2 == 0:
            print(number, end=' ')
            number = number + 1
        number = number + 1
    

def main():
    print_even_numbers(6, 20)
    print()
    print_even_numbers(7, 20)
    print()
    print_even_numbers(-9, 5)
    
main()
