'''
Many countries have 50 years as their standard length of copyrights
and when a work's copyright term ends, the work passes into the
public domain. Complete the function below which prints 
"Out of copyright" if the author has been dead 50 years or more.
'''
def copyright_check(current_year, author_death_year):
    if current_year - author_death_year > 50:
        print('Out of copyright')


def main():
    current_year = 2020
    author_death_year = input("Enter year of author's death: ")
    author_death_year = int(author_death_year)
    copyright_check(current_year, author_death_year)

main()
