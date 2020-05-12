'''
Define the required_boxes() function which is passed a total
number of items and the maximum number of items which fit into
one box. The function returns the total number of boxes required
(any leftovers always require an extra box).
'''

def required_boxes(items, per_box):
    boxes = items // per_box
    left_over = items % per_box
    extra = min(1, left_over)
    return boxes + extra

boxes_needed1 = required_boxes(30, 16)
boxes_needed2 = required_boxes(20, 3)
boxes_needed3 = required_boxes(30, 10)

print("1.", "Boxes:", boxes_needed1)
print("2.", "Boxes:", boxes_needed2)
print("3.", "Boxes:", boxes_needed3)
