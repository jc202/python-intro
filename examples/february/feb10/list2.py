#Author: Justin Chisholm
toys = [ "truck","car", "doll", "skipping rope" ,"train"]
print("Welcome to our toy store")

while True:
    command = input("(V)iew, (A)dd, (R)emove, (Q)uit: ").strip().lower()
    
    if command == "q":
        break
    elif command == "v":
        for toy in toys:
           print(f" -{toy}")
    elif command == "a":
        toy = input("Enter toy: ")
        toys.append(toy)
    elif command == "r":
        toy = input("Enter toy: ")
        toys.remove(toy)
        print(f"{toy} was removed.")
    else:
        print("Invalid Command")
print("Goodbye")