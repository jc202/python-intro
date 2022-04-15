#Author: Justin Chisholm
import random

print("Rolling our Dice")

while True:
    if input("Do you want to roll? ").lower().strip() != "y":
        break
    print(random.ranint(1,6))
    
print("Goodbye")