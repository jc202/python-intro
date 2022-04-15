def read_friends():
    friends = []
    
    with open("examples/mar29/friends.txt") as file:
        for line in file:
            friends.append(line.strip())
    return friends

def write_friends(friends):
    with open("examples/mar29/friends.txt", "w") as file:
        for friend in friends:
            file.write(f"{friend}\n")

def display_friends(friends):
    for friend in friends:
        print(f"- {friend}")

#read in our list
friends_list = read_friends()

#change list
print("Hey Friends!")

while True:
    command = input("(A)dd, (D)elete, (V)iew, (Q)uit: ").lower().strip()
    
    if command == "q":
        break
    elif command == "v":
        display_friends(friends_list)
    elif command == "a":
        friend = input("Enter friend name: ")
        friends_list.append(friend)
        print(f"{friend} was added to the list!")
        
#save list
write_friends(friends_list)
    