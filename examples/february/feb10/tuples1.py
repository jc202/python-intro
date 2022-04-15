#Author: Justin C
week_days = ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")

#most of the time we'd use this one
#for day in week_days:
#    print(day)

#if you want a counter
for i in range(len(week_days)):
    print(f"{i+1}. {week_days[i]}")
    
count = 1
for day in week_days:
    print(f"{count}. {day}")
    count+=1