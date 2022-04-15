#Author: Justin Chisholm
toys = {
    "doll" : 19.89,
    "car" : 1.99,
    "truck" : 7.85,
    "puzzle" : 14.89,
    "slinky" : 2
}

#print(toys{"truck"})
toys["yo-yo"] = 4.5

toy_name = input("Enter a toy name").strip().lower()
print(f"{toy_name} cost ${toys[toy_name]}")

# display all the toys
for toy_name in toys:
    print(f"{toy_name} costs ${toys[toy_name]}")