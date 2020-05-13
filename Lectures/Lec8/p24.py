'''
Complete the get_discount_message() function which returns a string
made up of the rate of discount, the string "% Discount: $", and the
discount amount. The function has two parameters, the discount
amount and the rate of discount (a whole number).
'''

def get_discount_message(discount_amt, rate):
    discount_info = str(rate) + '% Discount: $' + str(discount_amt)
    return discount_info

discount_message = get_discount_message(11.7, 5)
print(discount_message, sep='')
discount_message= get_discount_message(98.55, 15)
print(discount_message, sep='')
