'''
Complete the programm that prompts the user to enter a floatibg point value and
an unteger value and calculates and displays the value obtained when the floating point
value is raised to the power of the integer value. The result will be rounded to the
nearist 3 decimal places.
'''

number = float(input('Enter a floating point number: '))
power = int(input('Enter an integer: '))
obtained_value = round(number ** power, 3)

print(number, ' to the power of ', power, ' is ', obtained_value, sep = '')
