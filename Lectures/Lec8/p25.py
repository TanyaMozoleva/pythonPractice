'''
Complete the print_docket() function which prints the sales docket
information (the format should be as shown in the example output
shown). The function is passed two arguments, the price and the
discount rate (an int %). Your function code MUST make a call to both
the functions: get_discount() and get_discount_message().
'''
def get_discount(amount, discount_rate):
    discount = amount * discount_rate / 100
    return round(discount, 2)

def get_discount_message(discount_amt, rate):
    discount_info = str(rate) + '% Discount: $' + str(discount_amt)
    return discount_info

def print_docket(price, percent_rate):
    discount_amount = get_discount(price, percent_rate)
    discount_message = get_discount_message(discount_amount, percent_rate)
    final_price = price - discount_amount
    print('Original price $', price, sep='')
    print(discount_message)
    print('Price $',final_price, sep='')

print_docket(234, 5)
print()
print_docket(657, 15)
