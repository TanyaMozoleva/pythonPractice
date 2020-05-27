'''
def get_user_name(prompt):
    request = prompt + ': '
    user_name = input(request)
    return user_name

user_name = get_user_name('Enter name')

print('Hello' + ' ' + user_name)
'''
'''
def add_function(num1, num2):
    return num1 + num2

result = add_function(1,2)

print(result)

'''
'''
def say_hello(name='NAME'):
    return 'Hello ' + name

result = say_hello('Sally')

print(result)

def add(n1, n2):
    return n1 + n2 

result = add(20, 30)

print(result)
'''
'''
def dog_check(mystring):
    return 'dog' in mystring.lower():
    
print(dog_check('Dog ran away'))

'''
'''
def funny_latin(word):

    first_letter = word[0]

    #check if a vowel
    if first_letter in ['a', 'e', 'i', 'o','u']:
        new_word = word + 'ay'
    else:
        new_word = word[1:] + first_letter + 'ay'
    return new_word

print(funny_latin('apple'))

'''
'''
def myfunc(word):
    return word

result = myfunc('Hello world')
 
print(result)
'''
'''
def myfunc(name):
    return 'Hello ' + name

result = myfunc('Name')
print(result)
'''
'''
def myfunc(a):
    if a == True:
        return 'Hello'
    elif a == False:
        return 'Goodbye'

result = myfunc(False)
print(result)
'''
'''
def fun_2(age):
    years   = age + 10
    print('3.', years)

def fun_1(years):
    print('4.', years)
    years = 20

def main():
    years = 5
    fun_1(years)
    print('1.', years)
    fun_2(years)
    print('2.', years)

main()
'''

def function1():
    print("A")
    function2(3)
    print("B")

def function2(num):
    print("C")
    function4(num - 1, num - 2)
    print("D")

def function3(number):
    print("E", number)

def function4(num1, num2):
    print("F")
    function3(num1 + num2)
    
def main():
    print("G")
    function1()

main()
