'''
A year is a leap year if it is divisible by 400, or divisible by 4 but not
divisible by 100, e.g., 1900, 2011 and 2100 are not a leap years whereas
2000, 2008 and 2400 are leap years. Complete the is_leap_year()
function.
'''
def is_leap_year(year):
    if year % 400 == 0:
        return True
    if year % 4 == 0 and year % 100 != 0:
        return True
    else:
        return False

def main():
    print(is_leap_year(2011))
    print(is_leap_year(1900))
    print(is_leap_year(2100))
    print(is_leap_year(2000))
    print(is_leap_year(2008))
    print(is_leap_year(2018))
main()
