'''
Complete the add_bonus() function which prints "Good job!"
and returns 30000 plus the salary if the parameter is a value greater
than 150000. Otherwise it prints "Superb performance!" and returns
300 plus the salary.
'''

def add_bonus(salary):
    if salary >= 150000:
        print('Good job')
        salary = salary + 30000
    else:
        print('Super performance!')
        salary = salary + 300

    return salary

def main():
    salary = 34000
    new_salary = add_bonus(salary)
    print('Was: $' + str(salary), ' Now: $' + str(new_salary), sep='')
    print()
    salary = 250000
    new_salary = add_bonus(salary)
    print('Was: $' + str(salary), ' Now: $' + str(new_salary), sep='')
main()
