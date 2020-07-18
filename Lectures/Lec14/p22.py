'''
Complete the start_with_vowel_count() function
which returns the number of words in the list which start with
a vowel. Assume each word in the list has at least one letter.
'''

def end_with_vowel_count(a_list):
    vowels = "aeiouAEIOU"
    count = 0

    for word in a_list:
        if vowels.find(word[-1]) != -1:
            count = count + 1
    return count

def start_with_vowel_count(a_list):
    vowels = "aeiouAEIOU"
    count = 0

    for word in a_list:
        if vowels.find(word[0]) != -1:
            count = count + 1
    return count


def main():
    my_list = ['Nobody', 'goes', 'to', 'that', 'restaurant',
                            'because', 'it', 'is', 'too', 'crowded']

    vowel_starters = start_with_vowel_count(my_list)
    print("Start with a vowel", vowel_starters)

main()

