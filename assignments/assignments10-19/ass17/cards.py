#Author: Justin Chisholm
import random

def deal(card):
    cards =["ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "jack", "queen", "king"]
    
    if card == 1:
        return 1
    elif card ==2:
        return 2
    elif card ==3:
        return 3   
    elif card ==4:
        return 4   
    elif card ==5:
        return 5   
    elif card ==6:
        return 6   
    elif card == 7:
        return 7       
    elif card == 8:
        return 8  
    elif card == 9:
        return 9 
    elif card == 10:
        return 10 
    elif card == 11:
        return 11  
    elif card == 12:
        return 12  
    elif card == 13:
        return 13  

player_score = 0
pc_score = 0
print("Welcome to our Awesome Card Game!")

while True:
    player_card = deal(random.randint(1,13))
    pc_card = deal(random.randint(1,13))
    print(f"""
Computer Deals a Card: {pc_card}
You Deal a Card: {player_card}""")

    if player_card > pc_card:
        print("You won this round.")
        player_score += 1
    elif player_card < pc_card:
        print("Computer won this round.")
        pc_score += 1
    else:
        print("Tie")
    
    command = input("Would you like to play again? (Y)es or (N)o? ").strip().lower()
    if command == "n":
        break

print(f"""
Final Scores:
Player: {player_card}
Computer: {pc_card}

Goodbye.
""")
    
    



    


