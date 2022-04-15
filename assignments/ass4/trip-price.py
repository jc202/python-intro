#Author: Justin Chisholm
print("Let's see how expensive your trip will be!")

num_miles = float(input("How many miles will you travel: "))
num_days = int(input("How many days will you be traveling for: "))

#Variables (Costs)
gallon_price = 3.159 #price per gallon of gas
milespg = 24.9 #Miles per gallon on your car
breakfast = 10
lunch = 12.50
dinner = 20
hotel = 103.25

#hotel price 
hotel_total = hotel * num_days
#finding price of gas
gas_price = num_miles / milespg * gallon_price
#food
food = breakfast * num_days + lunch * num_days + dinner * num_days
#finding total travel costs
travel_cost = gas_price + food + hotel_total
print(f"{travel_cost}")

