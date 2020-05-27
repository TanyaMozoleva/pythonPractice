'''
Dedine the function which is passed two parameters:
 an integer (number_of_tickets), and a float , the price of each ticket.
 The function returns the total cost of the tickets rounded to the nearest whole number
'''

def get_ticket_price(number_of_tickets, ticket_price):
    full_price = abs(number_of_tickets * ticket_price)
    return round(full_price)

full_price = get_ticket_price(10,5)
print(full_price)

full_price = get_ticket_price(21, 7.50)
print(full_price + 5)
