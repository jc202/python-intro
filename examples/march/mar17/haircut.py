#Author: Justin Chisholm
def get_cut_cost(gender, length, density): 
    total = 0
    if gender == "m":
        total += 20
    else:
        total += 40
        
    if length == "l":
        total += 10

    if density == "t":
        total += 15
        
    return total

def get_color_cost(length, density, change):
    total = 50
    
    if length == "l":
        total += 20
    
    if density == "t":
        total += 20
    
    if change == "l":
        total += 50    
    
    return total

# Main Program
print("Salon Calculator")
gender = input("(M)ale or (F)emale: ").strip().lower()
length = input("Hair Length (L)ong or (S)hort: ").strip().lower()
density = input("Hair Density (F)ine or (T)hick: ").strip().lower()
cut = input("Hair Cut (Y)es or (N)o: ").strip().lower()
color =  input("Hair Color (Y)es or (N)o: ").strip().lower()

cost = 0

if cut == "y":
    cost += get_cut_cost(gender, length, density)

if color == "y":
    change = input("(L)ighter or (D)arker: ").lower().strip()
    cost += get_color_cost(length, density, change)
    
#tax
cost *= 1.07

print(f"Your estimated cost is ${round(cost, 2)}!")