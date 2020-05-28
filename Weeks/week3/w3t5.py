'''
the amount to be paid after the discount has been subtracted from the discount
'''

def display_ticket_price(tickets, price, discount):
    tickets_price = price - discount
    return tickets_price

def get_gst_amount(price):
    gst = (price / 100) * 15
    return round(gst, 2)


def get_sign_line(sign):
    sign = '*'
    sign_line = sign * 20
    return sign_line

display_ticket_price(4, 60, 6)

print(display_ticket_price)
print(get_sign_line)
print('Tickets: ', tickets, sep='')
print('Price: $', tickets_price, 'discount included: $', discount, sep='')
print('GST included: $', gst)
print(get_sign_line)

