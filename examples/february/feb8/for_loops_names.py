#Author: Justin C
import turtle
import random
turtle.setup(600,600)
turtle.bgcolor("lavender")
pen=turtle.Turtle()
pen.speed(0)
pen.color("black")
style = ("Arial", 12, "normal")
turtle.colormode(255)

user_name = turtle.textinput("Names", "Enter Name")
num_names = int(turtle.numinput("Names", "Enter Number of Names", 10, 1, 100))

for i in range(num_names):
    x = random.randint(-turtle.window_width()//2, turtle.window_width()//2)
    y = random.randint(-turtle.window_width()//2, turtle.window_width()//2)
    r = random.randint(0, 256)
    g = random.randint(0, 256)
    b = random.randint(0, 256)
    pen.color(r,g,b)
    
    pen.up()
    pen.setpos(x,y)
    pen.down()
    pen.write(user_name, font = style)


turtle.done()