'''
Define function which is passed a string as a parameter.
The function obtains an integer from the user using the parameter string as the prompt.
The function returns the integer entered by the user
'''

def get_number_from_user(prompt):
    return  int(input(prompt))

boxes = get_number_from_user('How many foxes are there? ')
print(boxes)
 
prompt = ('Enter number of tickets requied: ')
tickets = get_number_from_user(prompt)
print(tickets)

request = ('Enter age: ')
age = get_number_from_user(request)
print(age + 5)
print(tickets)

request = ('Enter age: ')
age = get_number_from_user(request)
print(age + 5)
