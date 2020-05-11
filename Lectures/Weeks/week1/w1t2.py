'''
The following formula can be used to calculate the monthly repayments that need to be made to pay off a house loan
'''

loan_amount = 650000
annual_interest_rate = 5
loan_length_years = 20
months_per_year = 12

month_interest_rate = annual_interest_rate / months_per_year
months = loan_length_years * months_per_year
percentage_of_rate = month_interest_rate / 100
numerator = percentage_of_rate * ( 1 + percentage_of_rate) ** months
denominator = ((1 + percentage_of_rate) ** months) - 1 
monthly_payment = loan_amount * (numerator / denominator)

print('You will need to pay $', round(monthly_payment), ' monthly', sep = '')
