'''
Define the get_inner_number function which is passed an integer as a parameter
and returns the integer made up of all the digits of the parameter number
 exept the first digit and the last digit.
 If the number parametr is a negative number, the function takes the absolute value of the paremeter number 
 and then proceeds as for a positive number
 If the number parameter consists of less then three digits, the function returns 0
'''
def get_inner_number(number):
    number = str(abs(number))
    return int('0' + number[1:-1])

print(get_inner_number(-24678))
print(get_inner_number(6))
print(get_inner_number(-19876))
