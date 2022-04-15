# Creating a mad libs game
# Author: Justin Chisholm

num1 = input("Number: ")
num2 = input("Second Number: ")
animal = input("Animal: ")
liquid = input("Liquid: ")
num3 = input("Third Number: ")
adj1 = input("First Adjective: ")
swt = input("Sweet Food: ")
num4 = input("Fourth Number: ")
adj2 = input("Second Adjective: ")

print(f"""
*** Mom's Cake Recipe ***

 First, preheat the oven to {num1} degrees. Then, beat {num2} {animal} egg(s) with a cup of {liquid}.
 Next, add {num3} teaspoon(s) of baking soda and mix with eggs and {liquid} until it reaches a {adj1} texture.
 Don't forget the {swt}! Pour into a 9 by 9 pan and bake for {num4} minute(s) or until the cake is {adj2}.
""")