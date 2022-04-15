#Author: Justin Chisholm
import turtle

turtle.bgcolor("skyblue")
turtle.setup(750,750)
pen = turtle.Turtle()
pen.speed(1)
pen.pensize(2)
pen.color("black")
pen.fillcolor("green")

shape = turtle.textinput("Shapes", "Enter Shape:").lower().strip()
if shape == "circle":
    pen.circle(50)
elif shape == "square":
    pen.forward(50)
    pen.left(90)
    pen.forward(50)
    pen.left(90)
    pen.forward(50)
    pen.left(90)
    pen.forward(50)
    pen.left(90)
elif shape == "triangle":
    pen.forward(50)
    pen.left(120)
    pen.forward(50)
    pen.left(120)
    pen.forward(50)
    pen.left(120)
else:
    turtle.write("Not a shape")
    
turtle.done()