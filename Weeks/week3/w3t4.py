'''
Define the function which is passed a float as a parameter.
The function returns the GST amount rounded to two decimal places.
The GST amount is 15% of the price parameter
'''

def get_gst_amount(price):
    gst = (price / 100) * 15
    return round(gst, 2)

gst = get_gst_amount(1000.75)
print(gst)

gst = get_gst_amount(250)
print(gst)

gst = get_gst_amount(380.0)
print(gst)


