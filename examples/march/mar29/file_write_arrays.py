friends = ["Amy", "Beth", "Carl", "Trish"]

with open("examples/mar29/friends.txt", "w") as file:
    for friend in friends:
        file.write(f"{friend}\n")