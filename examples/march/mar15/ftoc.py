#Author: Justin Chisholm
def fahr_to_cels(fahrenheit):
    celcius = (fahrenheit - 32) * 5/9
    return celcius

def cels_to_fahr(celcius):
    fahrenheit = (celcius * 9/5) + 32
    return fahrenheit

def miles_to_kilo(miles):
    kilometers = miles * 1.60934
    return kilometers

def kilo_to_miles(kilometers):
    miles = kilometers * 0.621371
    return miles

print("Conversion Program")
command = int(input(f"""
Enter type of Conversion:
1. fahrenheit to Celsius
2. Celsius to Fahrenheit
3. Miles to Kilometers
4. Kilometers to Miles
"""))

value = float(input("Enter Value: "))
result = 0
if command < 1 or command >4:
    print("Sorry, invalid command")
elif command == 1:
    result = fahr_to_cels(value)
    print(f"{value} F = (round{result, 2}) C")
elif command == 2:
    result = cels_to_fahr(value)
    print(f"{value} C = (round{result, 2}) F")
elif command == 3:
    result = miles_to_kilo(value)
    print(f"{value} miles = (round{result, 2}) kilometers")
elif command == 4:
    result = kilo_to_miles(value)
    print(f"{value} kilometers = (round{result, 2}) miles")
