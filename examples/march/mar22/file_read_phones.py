def get_phone_book():
    phone_list = {}
    
    with open("examples/mar22/phones.txt") as file:
        for line in file:
            data = line.split(',')
            name = data[0].lower().strip()
            phone = data[1].strip()
            phone_list[name] = phone
    return phone_list

def display_phone_book(phone_book):
    for name in phone_book:
        print(f"name: {phone_book[name]}")

def display_phone_number(phone_book, name):
    clean_name = name.lower().strip()
    if clean_name in phone_book:
        print(f"{name}'s number is {phone_book[clean_name]}")
    else:
        print(f"Sorry {name} is not in our phone book.")

phone_book = get_phone_book()

while True:
    command = input("(v)iew, Get (N)umber, (Q)uit: ").strip().lower()
    
    if command == "v":
        display_phone_book(phone_book)
    elif command == "n":
        name = input("Enter Name: ")
        display_phone_number(phone_book, name)
    elif command == "q":
        break
    else: 
        print("Sorry. Invalid Command.")
print("Goodbye")