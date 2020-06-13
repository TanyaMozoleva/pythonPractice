'''
For an integer, a divisor is a number which divides exactly into the
integer (a factor of the integer), e.g., the divisors of 6 are 1, 2, 3, 6.
Note that 1 and the number itself are divisors (they divide into the
number exactly). For this function we only want the sum of all the
divisors less than the number itself. Complete the function.
'''

def get_sum_of_divisors(number):
    divisor = 1
    sum_of_divisors = 0

    while divisor <= number // 2:
        if number % divisor == 0:
            sum_of_divisors = sum_of_divisors + divisor
        divisor = divisor + 1
    return sum_of_divisors

def main():
    print('get_sum_of_divisors(6)', get_sum_of_divisors(6))
    print('get_sum_of_divisors(24)', get_sum_of_divisors(24))
    print('get_sum_of_divisors(25)', get_sum_of_divisors(25))
    print('get_sum_of_divisors(5628)', get_sum_of_divisors(5628))
main()
