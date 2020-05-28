'''
obtain a number from the user( in the  function call use the request variable defined in the main)
calculate the cost of the items(including the handling)
print the cost details
'''
def get_number(prompt):
    return int(input(prompt))

def get_cost(number_of_items, cost_per_unit, handling_cost):
    total_cost = (number_of_items * cost_per_unit) + handling_cost
    return total_cost

def display_details(items, cost_each, handling_cost, final_price):
    print('Items: ', items, 'Cost per item: $', cost_each, sep='')
    print('Handling cost: $', handling_cost, sep='')
    print('Total: $', final_price, sep='')

def main():
    request = ('Enter number (5-20): ')
    items = get_number(request)
    display_details()

main()
