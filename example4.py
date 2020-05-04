'''
Write a program that converts a volume of 1571 ounces to the equivalent volume in gallons, pints and ounces. There are 8 pints in a gallon and 16 ounces in a print
'''

initial_ounces = 1571
ounces_in_pint = 16
pints_in_gallon = 8

ounces = initial_ounces % ounces_in_pint
whole_pints = initial_ounces // ounces_in_pint
gallons = whole_pints // pints_in_gallon
pints = whole_pints % pints_in_gallon

print(initial_ounces, ' ounces is equivalent to:', sep = '')
print(gallons, ' gallons, ', pints, ' pints and ', ounces, ' ounces ', sep = '')
