loan_amount = 650000
annual_interest_rate = 5
loan_length_years = 20
months_per_year = 12


month_interest_rate = annual_interest_rate / months_per_year
amount_of_months = loan_length_years * months_per_year
percent_of_rate = month_interest_rate / 100
numerator = percent_of_rate * ( 1 + percent_of_rate) ** amount_of_months
denominator = ((1 + percent_of_rate) ** amount_of_months) - 1 
monthly_payment = loan_amount * (numerator / denominator)


print('You will need to pay $', round(monthly_payment), ' monthly', sep = '')

