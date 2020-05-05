'''
Write a program which converts 500$ NZ to Australian
'''
amount_to_convert = 500
nz_to_aus_rate = 0.95
nz_dollars = amount_to_convert
aus_dollars = amount_to_convert

final_amount_nz = aus_dollars / nz_to_aus_rate
final_amount_aus = nz_dollars * nz_to_aus_rate

print('NZ $', nz_dollars, ' = ', 'AUS $' , final_amount_aus, sep = '')
print('AUS $', aus_dollars, ' = ', 'NZ $', final_amount_nz, sep = '')
