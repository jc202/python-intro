#Author: Justin Chisholm
import turtle
turtle.setup(600,600)
turtle.bgcolor("white")
pen=turtle.Turtle()
pen.speed(0)
pen.color("black")
pen.width(1)
pen.color("sky blue")

def draw_square(x, y, width, color):
    draw_rect(x, y, width, width, color)
    
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

#draw a house
def draw_house(x,y, width, body_color, roof_color):
    draw_square(x-width/2, y-width/2, width, body_color)
    draw_tri(x-width*.6, y+width/2, width * 1.2, roof_color)
    draw_rect(x-width* .15, y-width/2, width* .3, width * .6, roof_color)
    draw_circle(x+width * .05, y-width * .3, width* .05, body_color)
    
draw_house(-100, 50, 70, "violet", "gold")
draw_house(-0, 50, 70, "skyblue", "red")
draw_house(100, 50, 70, "yellow", "cyan")
turtle.done()