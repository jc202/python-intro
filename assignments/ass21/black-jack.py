#Author: Justin C
import random

def get_score():
    with open ("assignments/ass21/score.txt") as file:
        for line in file:
            score = int(line.strip())
        return score

def save_score(score):
    with open ("assignments/ass21/score.txt", "w") as file:
        file.write(f"{score}\n")

def play_round():
    user_hand = 0
    pc_hand = 0
    
    for i in range(2):
        rand_num = random.randint(1,11)
        user_hand += rand_num
    print(f" Your hand total: {user_hand}.")
    
    while True:
        if user_hand > 21:
            print("No more cards for you")
            return user_hand
        
        score = get_score()    
        command = input("Do you want another card? (Y)es or (N)o? ")
        
        if command == "y":
            rand_num = random.randint(1,11)
            user_hand += rand_num
            print(f" Your hand totals {user_hand}.")
        elif command == "n":
            rand_num = random.randint(14,23)
            pc_hand += rand_num    
            break
        
    print(f"Computer hand total: {pc_hand}.")    
    if user_hand >= pc_hand:
        score += 1
        save_score(score)
    elif user_hand == pc_hand:
        print("This round is a tie. Want to try again?")
    elif pc_hand <= pc_hand:
        score -= 1
        save_score(score)
        print("The Computer won this round. Why not give it another go?")
    return score
    
score = get_score()
score += 1

print(score)
#main program
print("Welcome to Math Fun!")


