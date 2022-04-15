import random


def get_score():
    with open("examples/mar29/score.txt") as file:
        lines = file.readlines()
        if not lines:
            return 0
        return int(lines.pop().strip())
    
def save_score(score):
    with open("examples/mar29/score.txt", "w") as file:
        file.write(f"{score}\n")

def sum_digits(number):
    sum = 0
    
    while number > 0:
        digit = number % 10
        sum += digit
        number = number // 10
    
    return sum

def play_round():
    
    rand_num = random.randint(1000,9999)
    ans = sum_digits(rand_num)
    
    user_ans = int(input(f"Sum the digits of {rand_num}: "))
    
    if ans == user_ans:
        return True
    else:
        print(f"Incorrect. The answer should be {ans}")
        return False
    
# Read in Score
score = get_score()

#Play game and modify score
print("Welcome to Math Fun!")

while True:
    command = input("(P)lay or (Q)uit: ").strip().lower()
    
    if command == "q":
        break
    elif command != "p":
        print("Sorry, Invalid Command.")
        continue
    
    if play_round():
        print("Yay! You got it!")
        score += 1
        
    
    print(f"Your current score is {score}")
    
    


#Save Score
save_score(score)