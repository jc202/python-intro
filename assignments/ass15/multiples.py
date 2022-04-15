#Author: Justin Chisholm
def sum(num):
    total = 0
    factors = []
    
    for factor in range(1, 100):
        total += 1
        if num % total == 0:
            factors.append(factor)
    print(f"The Factors of {num} are: {factors} ")

        
while True:
    command = input("Would you like to (L)ist Multiples or (Q)uit: ").strip().lower()
    
    if command == "q":
        break
    elif command == "l":
        num = int(input("Enter Number: "))
        sum(num)
