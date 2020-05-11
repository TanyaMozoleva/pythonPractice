'''
Complete the program that prompts the user to enter their name 
and then displays their name with the first name and family name swapped around
'''

prompt = input("Enter your name in the format first-name middle-name family-name: ")
first_space = prompt.find(' ')
second_space = prompt.rfind(' ')
first_name = prompt[:first_space]
middle_name = prompt[first_space + 1: second_space]
family_name = prompt[second_space +1:]
new_name = family_name + ' ' + middle_name + ' ' + first_name 

print('Your new name is ', new_name, sep = '')
