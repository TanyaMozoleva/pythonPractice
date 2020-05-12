'''
Complete the program that prompts the user to enter their name 
and then displays their name with the first name and family name swapped around
'''

name = input("Enter your name in the format first-name middle-name family-name: ")
first_space = name.find(' ')
second_space = name.rfind(' ')
first_name = name[:first_space]
middle_name = name[first_space + 1: second_space]
family_name = name[second_space + 1:]
new_name = family_name + ' ' + middle_name + ' ' + first_name 

print('Your new name is ', new_name, sep = '')
