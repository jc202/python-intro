#Author: Justin C
week_day = input("Enter day of the week: ").lower()

if week_day == "monday" or week_day == "mon":
    print("It's Moes Monday!")
elif week_day == "wednesday" or week_day == "wed":
    print("It's Wing Wednesday!")
elif week_day == "sunday" or week_day == "sun":
    print("It's Footbal Hour!")
else:
    print("Sorry, no deal today.")