'''
Write a program that converts a volume of 1571 ounces to the equivalent volume in gallons, pints and ounces. There are 8 pints in a gallon and 16 ounces in a print
'''

ounces = 1571
pints_in_gallon = 8
ounces_in_pint = 16
last_ounces = ounces % ounces_in_pint
pints = ounces / ounces_in_pint
last_gallons = pints / pints_in_gallon
last_pints = pints % pints_in_gallon

print('1571 ounces is equivalent to: ', '\n', round(last_gallons), ' gallons, ', round(last_pints), ' pints and ', last_ounces, ' ounces ', sep = '')
