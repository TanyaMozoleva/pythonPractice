'''
'''

def get_price(number_of_items, price_per_item):
    final_price = number_of_items * price_per_item

    if number_of_items <= 5:
        final_price = number_of_items * price_per_item
    elif number_of_items <= 9:
        final_price = final_price - (final_price * 0.1)
    elif number_of_items >= 10:
        final_price = final_price - (final_price * 0.2)
    
    return round(final_price)

def main():
    price = get_price(3, 5.0)
    print('$' + str(price), sep='')
    print('$' + str(get_price(10, 15.0)))
    print('$' + str(get_price(31, 0.5)))

main()
