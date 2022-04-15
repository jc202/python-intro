#Author: Justin Chisholm
from datetime import date, time, datetime

todays_date = date.today()

print(todays_date.strftime("%A %B %d, %Y"))

halloween = date(2022, 10, 31)
print(halloween.strftime("%m/%d/%Y"))

class_time = time(8, 30)
print(class_time.strftime("%H %M %p"))

pie_day = datetime(2022, 3, 14, 13, 59)
print(pie_day.strftime("%m.%d.%I.%M"))

birthday_text = input("Enter Birthday (Enter Birthday (MM/DD/YYYY)").strip()
birthday = datetime.strptime(birthday_text, "%m/%d/%Y")
print("Your birthday is " + birthday.strftime("%B %d"))

# how long till pie day
days_till_pie = (pie_day - datetime.now()).days
print(f"You have {days_till_pie} days till pie day!")