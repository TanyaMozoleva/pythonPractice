'''
'''

def remove_spaces(phrase):
    index = 0 
    while  index < len(phrase):
        if phrase[index] == ' ':
            phrase = phrase[:index] + phrase[index + 1:]
        else:
            # index += 1
            index = index + 1
    return phrase

def main():
    result = remove_spaces('1 5 67 88')
    print(result)
    print(remove_spaces('programming is such fun, fun, fun'))
    print(remove_spaces('1 5 67 88    '))

main()
