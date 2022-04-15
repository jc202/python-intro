#Author: Justin C
shoes = []
print("Shoe Inventory")
shoe = input("Enter shoe: ")
shoes.append(shoe)

while True:
    command = input("Do you have more shoes to add, (Y)es or (N)o: ").strip().lower() 
    if command == "y":
        shoe = input("Enter shoe: ")
        shoes.append(shoe)
    elif command == "n":
        print("Here is your inventory:")
        for shoe in shoes: 
            print(f"-{shoe}")
        break
