'''
Write a program, that prompts the user to enter ther name and then displays their name, in uppercase,
as part of a banner.
'''

sign = '#'
first_name = input('Enter your first name: ')
family_name = input('Enter your family name: ')
full_name = first_name.upper() + ' ' + family_name.upper()
line_of_signs = sign * len(full_name)

print(line_of_signs)
print(full_name)
print(line_of_signs)
