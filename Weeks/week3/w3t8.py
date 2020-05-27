'''
Define the function which is passed three parameters. 
an integer - the number of items
a float - the price of each item
a float - the amount paid
The function calculates and returns the change(rounded to two decimal places) after all the items have been paid for
'''

def get_change(items, price_per_item, amount_tendered):
    total_cost = items * price_per_item
    change = amount_tendered - total_cost
    return round(change, 2)

change = get_change(3, 5.0, 20.0)
print('$' + str(change))
print('$' + str(get_change(2, 2.5, 5.0)))
print('$' + str(get_change(7, 1.5, 50.0)))
