'''
Write a program that prompts the user to enter a word. 
In then prints a new word where the first and last characters of the word
entered by the user are swapped.
'''

word = input('Enter a word: ')
first_character = word[0]
last_character = word[-1]
middle_slice = word[1:-1]
new_word = last_character + middle_slice + first_character

print('The new word is ', new_word, sep = '')
