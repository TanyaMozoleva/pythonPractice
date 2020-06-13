'''
'''

def get_letter(word):
    print(word)
    prompt = 'Enter index: '
    index = int(input(prompt))

    while index < 0 or index > len(word) - 1:
        index = int(input(prompt))
        
    return word[index]

def main():
    letter = get_letter('Dreams')
    print(letter)
    print(get_letter('programming'))
    print(get_letter('Huh!'))

main()
