'''
'''

def remove_digit_nine(number_str):
    index = number_str.find('9')
    
    while index != -1: 
        number_str = number_str[:index] + number_str[index + 1:]
        index = number_str.find('9')
    
    return number_str

def main():
    result = remove_digit_nine('23994596') # 8
    print(result)
    print(remove_digit_nine('-3459'))
    print(remove_digit_nine('-99000'))
    print(remove_digit_nine('12334'))

main()
