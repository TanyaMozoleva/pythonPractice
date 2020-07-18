'''
An amount doubles each year. Using a for...in range()
loop complete the double_each_year() function which
prints the growth of the parameter, (start_amt)
for the given number of years (num_years).
The first line printed by the function is the starting
amount. Each line of the output is numbered starting
from the number 1. The function returns the final
amount.
'''

def double_each_year(start_amt, num_years):
    print('Starting with: ',start_amt , sep='')
    amount = start_amt #24
    for number in range(1, num_years + 1): #1 2 3 4 
        amount = amount * 2 #48
        print(number, ':', amount, sep='')


    return amount


def main():
    print("After 4 years:",double_each_year(24, 4))
    print("After 3 years:", double_each_year(235, 3))
    print("After 5 years:", double_each_year(15, 5))

main()
