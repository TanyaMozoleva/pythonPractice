'''
Define the get_result1() function which is passed three whole numbers.
The functions returns the sum of the two bigger numbers
'''

def get_result1(num1, num2, num3):
    smallest = min(num1, num2, num3)
    result = num1 + num2 + num3 - smallest
    return result

print('1. ', get_result1(1, 2, 3))
print('2. ', get_result1(11, 12, 3))
print('3. ', get_result1(6, 2, 5))
