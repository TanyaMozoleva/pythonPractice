'''
Complete the following program  so that it prints the name between two rows of stars. The output has three spaces on each side of the name
'''
name = 'Philomena Evangeline'
extras = 3
symbol = '*'

lots_of_symbols = symbol * 26

print(lots_of_symbols)
print(' ' * extras, name, ' ' * extras, sep = '')
print(lots_of_symbols)
