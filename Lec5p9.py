'''
Complete the following program so that it prints the initial from the first
name followed by a full stop, a space and followed by the surname.
Assume the full name is always two names separated by a single space.
'''
full_name = "Wystan Auden"

space_index = full_name.find(' ')
first_name = full_name[: space_index]
last_name = full_name[space_index + 1 :]
first_letter = first_name[0]
initialled_name = first_letter + ". " + last_name

print(initialled_name)
