#Author: Justin Chisholm
#Author: Justin C
import turtle
turtle.setup(600,600)
turtle.bgcolor("white")
pen=turtle.Turtle()
pen.speed(0)
pen.color("black")
pen.width(1)
pen.color("sky blue")

def draw_square(x, y, width, color):
    draw_rect(x, y, width, color)
    
def draw_tri(x, y, width, color):
    pen.color(color)
    pen.up()
    pen.setpos(x,y)
    pen.down()
    
    pen.begin_fill()
    for i in range(3):
        pen.forward(width)
        pen.left(120)
    pen.end_fill()

def draw_rect(x, y, length, width, color):
    pen.color(color)
    pen.up()
    pen.setpos(x,y)
    pen.down()
    
    pen.begin_fill()
    for i in range(4):
                if i % 2 == 0:
                    pen.forward(length)
                else:
                    pen.forward(width)
                pen.left(90)
    pen.end_fill()

def draw_circle(x, y, radius, color):
    pen.color(color)
    pen.up()
    pen.setpos(x,y)
    pen.down()
    pen.begin_fill()
    pen.circle(radius)
    pen.end_fill()


turtle.done()