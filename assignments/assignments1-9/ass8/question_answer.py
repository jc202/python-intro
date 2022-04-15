#Author: Justin C
import random


print("Welcome to the Super Fun Question Game!!!")
q1 = input("Ask a yes or no question: ") #q1 = question one
num = random.randint(1,3)

#original if statement
if num == 1:
    print("Yes")
elif num == 2:
    print("No")
elif num == 3:
    print("Maybe")
    
#creating the loop!
q2 = input("Would you like to ask another question? (Y)es or (N)o: ").lower().strip()
while q2 == "yes" or q2 == "y":
    print("Great! Let's play again.")
    q1 = input("Ask a yes or no question: ")
    num = random.randint(1,3)
    if num == 1:
        print("Yes")
    elif num == 2:
        print("No")
    elif num == 3:
        print("Maybe")
    q2 = input("Would you like to ask another question? (Y)es or (N)o: ").lower().strip()
        
print("Alright. Have a good day!")

#correct answer below, reviewed in class
#Author: Justin C
import random


#loop
#rather than the variable "Play Again", you could just delete
#-the variablee and just use "while true"
play_again = "y"

while play_again == "y":
    #ask question
    input("Enter a question: ")
    #display random answer
    rand_num = random.randint(1,3)
    if rand_num == 1:
        print("yes")
    elif rand_num == 2:
        print("No")
    else:
        print("Maybe")
    #ask play again
    if input("Ask Another question: ").trim().lower() != "y":
        break
print("Goodbye")