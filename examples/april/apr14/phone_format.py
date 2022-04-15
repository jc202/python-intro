#Author: Justin C
#original phone format (803) - 123 - 4567
#new phone format 803.123.4567

def update_phone(phone):
    answer = ""
    
    for letter in phone:
        if letter == "(" or letter == ")":
            continue
        elif letter == "-":
            answer += "."
        else:
            answer += letter
    
    return answer


phone = update_phone("(803)-123-4567")
print(phone)