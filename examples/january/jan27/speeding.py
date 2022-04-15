#Author: Justin Chisholm
print("You just got pulled over!")
speed = int(input("Enter your speed: "))

if speed >90: 
    print("Jail Time.")
elif speed>80:
    print("Ticket Time.")
elif speed >70:
    print("This is a Warning!")
elif speed <25:
    print("Jail - too slow.")
elif speed <45:
    print("Ticket - too slow")


    
else:
    print("You are a good person.")
    
print("Have a nice day!")