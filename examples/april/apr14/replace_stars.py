from ctypes.wintypes import WORD


def replace_stars(): 
    global Word
    answer = ""
    
    for letter in word:
        if letter == "*":
            answer += "."
        else:
            answer += letter
    
    word = answer
    
    
word ="happy* I love*****"
replace_stars()
print(word)