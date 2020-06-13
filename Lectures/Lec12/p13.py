'''
A perfect number is an integer that is equal to the sum of its divisors
(including 1, excluding the number itself), e.g., the sum of the divisors of
28 is 28 (1 + 2 + 4 + 7 + 14). Complete the check_perfection()
function which checks for perfection and prints either '#is a
perfect number' or '#is NOT a perfect number'.
'''

def get_sum_of_divisors(number):
    divisor = 1
    sum_of_divisors = 0
    while divisor <= number // 2:
        if number % divisor == 0:
            sum_of_divisors = sum_of_divisors + divisor
        divisor = divisor + 1 
    return sum_of_divisors

def check_perfection(number):
    message_is = ' is a perfect number'
    message_is_not = ' is NOT a perfect number'
    sum_of_divisors = get_sum_of_divisors(number)

    if number == sum_of_divisors:
        print(number, message_is, sep='')
    elif number != sum_of_divisors:
        print(number, message_is_not, sep='')

def main():
    check_perfection(28)
    check_perfection(54)
    check_perfection(496)
    check_perfection(100)
    
main()
