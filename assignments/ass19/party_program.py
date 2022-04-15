def get_boolean(value):
    if value == "true":
        return True
    if value == "false":
        return False              
        
def get_guests():
    names = {}
    
    with open("assignments/ass19/guest_list.txt") as file:
        for line in file:
            data = line.split(':')
            name = data[0].lower().strip()
            value = get_boolean(data[1].strip())
            names[name] = value
    return names

def display_guests(guests, coming):
    for guest in guest_list:
        if guest_list[guest] == coming:
            print(guest)

guest_list = get_guests()


while True:
    command = input("View (A)ttending, (N)ot Attending, (Q)uit: ").strip().lower()
    
    if command == "q":
        break
    elif command == "a":
        print("Guests coming: ")
        display_guests(guest_list, True)
    elif command == "n":
        print("Guests not coming: ")
        display_guests(guest_list, False)
    else:
        print("Invalid Command. Please try Again.")
        
print("Goodbye.")