'''
Complete the following program that calculates the number of days, hours and minutes in 65601 minutes.
'''


number_of_minutes = 65601
minutes_per_hour = 60
hours_per_day = 24

amount_of_minutes_per_day = hours_per_day * minutes_per_hour

amount_of_days = number_of_minutes // amount_of_minutes_per_day

amount_of_minutes_left_over = number_of_minutes % amount_of_minutes_per_day

amount_of_hours = amount_of_minutes_left_over // minutes_per_hour

amount_of_minutes = amount_of_minutes_left_over % minutes_per_hour


print(amount_of_minutes_per_day)

print(amount_of_days)


print(amount_of_minutes_left_over)

print(amount_of_hours)

print(amount_of_minutes)

print(number_of_minutes, ' ', 'minutes', ' ', '=', ' ', amount_of_days, ' ', 'days', ' ', amount_of_hours, ' ', 'hours', ' ', 'and', ' ', amount_of_minutes, ' ', 'minutes', sep ='')

