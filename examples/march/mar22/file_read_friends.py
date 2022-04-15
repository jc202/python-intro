def get_friends():
    friends = []
    with open("examples/mar22/friends.txt") as file:
        for line in file:
            friends.append(line.strip().lower())
        return friends
        
people = get_friends()
print("Party Time")

while True:
    command = input("(C)heck Guests, (L)ist Guests, (Q)uit: ").strip().lower()
    
    if command == "q":
        break
    elif command == "c":
        name = input("Enter name: ").strip().lower()
        if name in people:
            print("Welcome")
        else:
            print("Sorry, you are not invited")
    elif command == "l":
        print("Friends: ")
        for person in people:
            print(person)
    else:
        print("Invalid Command. Please Try Again.")