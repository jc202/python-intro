def factorial(num):
    ans = 1
    
    for i in range(1, num+1):
        ans *=i
        
        
    print(f"{num}! = {ans}")

factorial(5)