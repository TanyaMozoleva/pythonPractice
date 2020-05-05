'''
Heron's formula
'''
import math

side1 = 4
side2 = 7
side3 = 9
#Complete the code
result1 = side1 ** 2 * side2 ** 2 + side1 ** 2 * side3 ** 2 + side2 ** 2 * side3 ** 2
result2 = side1 ** 2 + side2 ** 2  + side3 ** 2
result3 = (4 * result1 - result2 ** 2) ** 0.5
area = result3 / 4

print('Length of sides: ', side1, ', ', side2, ' and ', side3, sep = '')
print(result1, result2, result3)
print('Area:', area)
