'''
Define the function which is passed two parameters: an integer(the_number_of_tickets) 
and a float,the total price of the tickets (total_price).
The function returns thr discount amount rounded to the nearest whole number/
The discount is the bigger of the following two calculations:
either $4 discount for each ticket
or 10% of the total price
'''

def get_discount(number_of_tickets, total_price):
    discount_from_tickets = number_of_tickets * 4
    discount_from_total_price = (total_price / 100) * 10
    discount = max(discount_from_tickets, discount_from_total_price)
    return round(discount)


discount = get_discount(11, 1000.75)
print(discount)

discount = get_discount(5, 250)
print(discount)

discount = get_discount(3, 380.0)
print(discount)
