#Author: Justin C
debt_name = []
debt_amount = []

while True:
    command = input("(V)iew, (A)dd, (R)emove, (Q)uit: ").strip().lower()
    
    if command == "v":
        for debt in debt_name:
           print(f"- {debt}: ${value}")
    elif command == "a":
        debt = input("Enter Debt Name: ")
        debt_name.append(debt)
        value = input("Enter Debt Amount: ")
        debt_amount.append(value)
    elif command == "r":
        print("Why not buy a box of donuts instead? :)")
    elif command == "q":
        break
    else:
        print("Invalid Command. Please Try Again.")
print("Goodbye")