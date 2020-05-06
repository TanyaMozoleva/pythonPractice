'''
Complete the following program so that it prints the total tax and the net
pay rounded to a whole number. The first $14000 is not taxed. The next
amount up to $38500 is taxed at 24% and the rest is taxed at 34%.
'''

salary = 54000
no_tax_boundary =  14000
rate1_boundary = 38500
rate1 = 0.24
rate2 = 0.34

rate1_amount = rate1_boundary - no_tax_boundary
rate2_amount = salary - rate1_boundary
tax_rate1 = round(rate1_amount * rate1)
tax_rate2 = round(rate2_amount * rate2)
total_tax = tax_rate1 + tax_rate2
net_pay = salary - total_tax

print("Salary: $", salary,sep="")
print("Amount to be taxed at: 24%: $", rate1_amount, sep="")
print("Tax at rate 1: $", tax_rate1,sep="")
print("Amount to be taxed at: 34%: $", rate2_amount, sep="")
print("Tax at rate 2: $", tax_rate2, sep="")
print("==================================")
print("Total tax: $", total_tax, sep = "")
print()
print("Net pay: $", net_pay, sep = "")
print("==================================")
