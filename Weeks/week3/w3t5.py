'''
the amount to be paid after the discount has been subtracted from the discount
'''

def display_ticket_price(tickets, price, discount):
    tickets_price = price - discount
    gst = get_gst_amount(tickets_price)
    print(get_sign_line('*', 20))
    print('Tickets: ', tickets, sep='')
    print('Price: $', tickets_price, ' (discount included: $', discount, ').', sep='')
    print('GST included: $', gst, sep='')
    print(get_sign_line('*', 20))
    

def get_gst_amount(price):
    gst = (price / 100) * 15
    return round(gst, 2)


def get_sign_line(sign, length):
    return sign * length

display_ticket_price(4, 60, 6)
