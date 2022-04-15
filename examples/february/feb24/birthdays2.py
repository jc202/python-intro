#Author: Justin Chisholm
from datetime import date

birthdays = {
    "Barbara" : date(2022, 5, 13),
    "John" : date(2022, 4, 30),
    "Debra" : date(2022, 2, 26),
    "Dave" : date(2022, 9, 15),
    "Frank" : date(2022, 7, 10),
    "Nina" : date(2022, 6, 1),
}

#loop through the birthdays
for friend in birthdays:
    days_till = (birthdays[friend] - date.today()).days
    print(f"{friend}'s birthday is {friend} - {days_till} days away!")