'''
'''

def test_string(phrase):
    first_symbol = phrase[0].lower()
    last_symbol = phrase[-1].lower()
    vowels = 'aeiou'
    index1 = vowels.find(first_symbol)
    index2 = vowels.find(last_symbol)

    return (index1 != -1 or index2 != -1) and len(phrase) % 2 == 0
       

def main():
    result = test_string('Antonid')
    print(result)
    print(test_string('Anatonis'))
    print(test_string('PD'))

main()
