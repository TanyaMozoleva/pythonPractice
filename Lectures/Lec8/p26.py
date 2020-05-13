'''
The following program prompts the user for a number of items to be
packaged. Each box can hold 10 items. Any left over items require an
extra box. The first 6 boxes cost $8 each and any boxes above the first
6, cost $5 each. The program executes as shown in the example
outputs below. Design the functions needed to write this program
and write the main code for this program, i.e., the"brains" of the
program.
'''
def get_number_of_items(prompt):
    return int(input(prompt))

def cost_of_items(boxes):
    first_6 = min(boxes, 6)
    above_6 = boxes - 6
    above_6 = max(above_6, 0)
    cost = first_6 * 8 + above_6 * 5 
    return cost

def required_boxes(number_items, items_per_box):
    required_boxes = number_items // items_per_box
    left_over_items = number_items % items_per_box
    box_for_left_overs = min(left_over_items, 1)
    required_boxes = required_boxes + box_for_left_overs
    return required_boxes

def display_costs(items, boxes, packaging_cost):
    print('Items: ', items, sep='')
    print('Boxes needed: ', boxes, sep='')
    print('Cost: $', packaging_cost, sep='')

print()
items_per_box = 10
items = get_number_of_items('Enter number of items: ')
boxes = required_boxes(items, items_per_box)
cost = cost_of_items(boxes)
display_costs(items, boxes, cost)

print()
