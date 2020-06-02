'''
Complete the get_price() function which returns the cost of tickets.
If the total number of tickets is 14 or more, a 10% discount applies.
'''
def get_price(child, adult):
    child_price = 10
    adult_price = 25
    discount_size = 14
    discount_rate = 0.9

    cost = (child * child_price + adult * adult_price)
    if child + adult > discount_size:
        cost = cost * discount_rate 
    
    return cost

def main():
    num_child = int(input("Enter the number of children: "))
    num_adult = int(input("Enter the number of adults: "))
    cost = get_price(num_child, num_adult)
    print("The cost of your tickets is: $" + str(cost))

main()
