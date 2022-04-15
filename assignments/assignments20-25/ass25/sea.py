#Author: Justin C
from boat import Boat
import turtle
import random
turtle.setup(600,600)
pen = turtle.Turtle()
pen.speed(2)
pen.pensize(2)
turtle.bgcolor("skyblue")

colors = ["aqua", "yellow", "salmon", "springgreen", "orange", "orchid"]
boats = []

#main program
for i in range(10):
    x = random.randint(-turtle.window_width()//3, turtle.window_width()//3)
    y = random.randint(-turtle.window_height()//3, turtle.window_height()//3)
    width = random.randint(50, 200)
    boats.append(Boat(x, y, random.choice(colors), width))

for boat in boats:
    boat.draw(pen)
    
    
turtle.done()