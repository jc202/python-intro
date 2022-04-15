temp = int(input("Enter Temperature: "))
precip = input("Enter Precipitation: ").lower().strip()

if temp <= 32 and precip == "s":
    print("Wear a snow suit today.")
elif temp <=70 and precip == "r":
    print("Wear a rain jacket today.")
elif temp <=80 and precip == "r":
    print("Wear a swimsuit.")
else:
    print("No worries today. Wear what you'd like!")