#read the number in the file
with open ("examples/mar29/test.txt") as file:
    for line in file:
        num = int(line.strip())
        break

#adding to number
num += 1

#overwriting the number in the file with a new one
with open ("examples/mar29/test.txt", "w") as file:
    file.write(f"{num}\n")