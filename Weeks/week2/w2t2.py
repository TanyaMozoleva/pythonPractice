'''
Complete the programm that prompts thr user to enter a floatibg point value and
an unteger value and calculates and displays the value obtained when the floating point
value is raised to the power of the integer value. The result will be rounded to the
nearist 3 decimal places.
'''

prompt1 = input('Enter a floating point number: ')
prompt1 = float(prompt1)
prompt2 = input('Enter an integer: ')
prompt2 = int(prompt2)
obtained_value = prompt1 ** prompt2
obtained_value = round(obtained_value, 3)

print(prompt1, ' to the power of ', prompt2, ' is ', obtained_value, sep = '')
