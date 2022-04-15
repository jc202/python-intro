#Author: Justin C

toys = ["car", "truck", "doll", "train", "lego"]
#print(toys[3])
toys.append("skipping rope")

#toys=[]
#toys.append("car")
#toys.append("truck")

# Create a for loop that displats numers 0 - 4
#for i in range(len(toys)):
#    print(toys[i])

for item in toys: #you could also say for toy in toys. its a made up variable.
    print(f"- {item}")