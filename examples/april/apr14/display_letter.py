def display_letters(word):
    for i in range(len(word)):
        print(word[i])
        

def display_star_word(word):
    print("*", end ="")
    
    for letter in word:
        print(letter + "*", end="")
    
    print()
    
def in_word(word, letter):
    for l in word:
        if l == letter:
            return True
    return False

if in_word("star", "r"):
    print("Yay!")
else:
    print("Nay!")