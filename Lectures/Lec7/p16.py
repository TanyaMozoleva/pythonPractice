'''
Define the get_result2() function which is passed two strings.
The function returns the number of characters in the longer of the
two strings.
'''
def get_result2(word1, word2):
    length1 = len(word1)
    length2 = len(word2)
    return max(length1, length2)

print("1.", get_result2("Flibbertigibbet", "Rigmarole"))
print("2.", get_result2("Mollycoddle", "Cat"))
print("3.", get_result2("Skullduggery", "Canoodle"))
