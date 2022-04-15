#Author: Justin Chisholm
from datetime import date

birthdays = [date(2022, 11, 1), date(2023, 1, 22), date(2022, 3, 14), date(2022, 7, 11), date(2022, 8, 18), date(2022, 5, 2)]

#loop through and display birthdays
for birthday in birthdays:
    days_away = (birthday - date.today()).days
    print(f"{birthday.strftime('%B %d')} - {days_away} days away!")
    # you can only use one pair of double quotes! use single quotes for the rest! or it will be red!