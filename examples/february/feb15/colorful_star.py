#Author: Justin C
import turtle
import random
turtle.setup(600,600)
turtle.bgcolor("black")
pen = turtle.Turtle()
pen.speed(0)
pen.color("black")
pen.width(5)

colors = ("medium blue", "chartreuse", "cyan", "orange", "red", "lime", "purple", "tomato", "yellow", "orange")

for i in range (100):
    x = random.randint(-turtle.window_width()//2, turtle.window_width()//2)
    y = random.randint(-turtle.window_height()//2, turtle.window_height()//2)
    star_width = random.randint(20,60)
    star_color = random.choice(colors)
    pen.color(star_color)
    
    pen.up()
    pen.setpos(x,y)
    pen.down()
    
    #draw up triangle
    pen.begin_fill()
    for i in range(3):
        pen.forward(star_width)
        pen.left(120)
    pen.end_fill()
    
    pen.up()
    pen.setpos(x, y+star_width / 2)
    pen.down()
    
    #bottom triangle
    pen.begin_fill()
    for i in range(3):
        pen.forward(star_width)
        pen.left(-120)
    pen.end_fill()


turtle.done()