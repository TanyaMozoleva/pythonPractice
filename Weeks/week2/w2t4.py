'''
Write a program that prompts the user o enter a positive floating point value and
a negative floating point value. This program will calculate the square  of these values
 and the prints the absolute difference of the squares rounded to two decimal places
'''

positive_float = float(input('Enter a positive float: '))
negative_float = float(input('Enter a negative float: '))
square_of_the_positive_float = positive_float ** 2 
square_of_the_negative_float = negative_float ** 2 
difference_between_squares = round(abs(square_of_the_positive_float - square_of_the_negative_float), 2)

print('The absolute difference of the squares is ', difference_between_squares, sep = '')
