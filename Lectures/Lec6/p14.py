import random

first_name = input('Enter_name: ')
index = random.randrange(0, len(first_name))
first_name = first_name[:index] + first_name[index + 1 :]

print(first_name)
print(index)
