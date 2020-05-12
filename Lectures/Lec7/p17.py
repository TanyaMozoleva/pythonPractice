'''
Define the get_result3() function which is passed one string.
The function returns a string made up of the last character followed
by the first character (both in uppercase characters).
'''

def get_result3(word):
    first_letter = word[0]
    last_letter = word[-1]
    letters = last_letter.upper() + first_letter.upper()
    return letters

print("1.", get_result3("crudivorE"))
print("2.", get_result3("OrnerY"))
print("3.", get_result3("brouhaha"))
