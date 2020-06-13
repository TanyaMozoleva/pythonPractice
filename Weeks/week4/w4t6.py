'''
'''

def test_number(number):
    if number % 2 == 0 and 30 <= number <= 50:
        return True
    else: 
        return False

def main():
    result = test_number(33)
    print(result)
    print(test_number(28))
    print(test_number(30))

main()
