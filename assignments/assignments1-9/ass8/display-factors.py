#Author: Justin C

#Getting variables out of the way
print("Let's Count Factors!")
num = int(input("Enter a number: "))


for i in range (1, num + 1):
    if num % i == 0:
        print (f"- {i}")
    
        

