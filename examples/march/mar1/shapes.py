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
    pen.color(color)
    pen.up()
    pen.setpos(x,y)
    pen.down()
    
    pen.begin_fill()
    for i in range(4):
        pen.forward(width)
        pen.left(90)
    pen.end_fill()

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
    

#square 2
draw_square(-200,50, 75, "blue")
#triangle
draw_tri(10, 10, 40, "yellow")

turtle.done()