'''
'''

def get_feedback(mark, out_off):
    percentages_of_mark = round((mark * 100) // out_off, 1)

    if percentages_of_mark >= 80:
        return 'Exellent'
    elif percentages_of_mark >= 60:
        return 'Good'
    elif percentages_of_mark >= 50:
        return 'Pass'
    return 'Not a pass'

def main():
    feedback = get_feedback(15, 20)
    print(feedback)
    print(get_feedback(100, 200))
    print(get_feedback(65, 90))

main()
