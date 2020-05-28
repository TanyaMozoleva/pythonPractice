'''
'''

def get_first_last_number(number):
    number = str(abs(number))
    first_last_number = number[0] + number[-1]
    return int(first_last_number)

print(get_first_last_number(24678))
print(get_first_last_number(6))
print(get_first_last_number(-19876))
print(get_first_last_number(0))

