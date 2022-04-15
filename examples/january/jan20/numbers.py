# Author: Justin Chihsolm
import math

# Incrementing Age
age = float(input("Enter Age: "))
decade = 10 
future_age = age + decade 
print(f"Your future age is {future_age}")

#Pizza Party
print("We're having a pizza party!!!")
num_guests = int(input("Enter number of guests: "))
avg_slices = float(input("Enter Average slicers per guest: "))
total_slices = num_guests * avg_slices
num_pizzas = math.ceil(total_slices / 8)
print(f"You should order {num_pizzas} pizzas!")

# Chickens and eggs
num_eggs = int(input("How many eggs did you collect: "))
num_cartons = num_eggs // 12 #rounded down
eggs_left = num_eggs - num_cartons * num_eggs
eggs_left = num_eggs % 12 #remainder after division
print(f"You need {num_cartons} cartons.")
print(f"You have {eggs_left} eggs left over.")

# Wages
hourly_wage = float(input("How much do you get paid per hour: "))
#ot_wage = hourly_wage * 1.5
hourly_wage *= 1.5
print(f"You should make ${round(hourly_wage, 2)} in overtime! Have a good day at work!")
