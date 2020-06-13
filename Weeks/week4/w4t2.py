'''
  define
'''

def get_ticket_price(number_of_tickets, price_per_ticket, has_discount, is_a_member):
    total_price = number_of_tickets * price_per_ticket   
    coefficient = 1

    if is_a_member and has_discount:
        coefficient = 0.8
    elif not is_a_member and has_discount:
        coefficient = 0.85
    elif is_a_member and not has_discount:
        coefficient = 0.9

    return round(total_price * coefficient)

def main():
    price = get_ticket_price(5, 20, True, False)
    print('$' + str(price), sep='')
    print('$' + str(get_ticket_price(5, 20, False, True)), sep='')
    print('$' + str(get_ticket_price(5, 20, False, False)), sep='')

main()
