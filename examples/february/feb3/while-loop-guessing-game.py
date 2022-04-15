#Author: Justin C
import random

goal = random.randint(1,100)
num_guesses = 1


print("Welcome to our guessing game")
guess = int(input("Enter number between 1 and 100: "))

while guess != goal:
    print(f"Sorry, {guess} is not the answer.")
    
    if guess < goal:
        print(f"{guess} is too low.")
    else:
        print(f"{guess} is too high.")
    guess = int(input("Enter number between 1 and 100: "))
    num_guesses += 1
print(f"You got it in {num_guesses}! The number was {goal}")