'''
Complete the get_discount() function which returns the discount
amount (a float rounded to 2 decimal places). The function is passed
two parameters, the amount and the discount rate (an integer %).
'''

def get_discount(amount, discount_rate): 
    discount = amount * discount_rate / 100
    return round(discount, 2) 

discount_message = 'Discount: $' + str(get_discount(234, 5))
print(discount_message, sep='')
discount_message = 'Discount: $' + str(get_discount(125, 15))
print(discount_message, sep='')
