#Author: Justin Chisholm
import turtle
import random
turtle.setup(600,600)
turtle.bgcolor("grey")
pen=turtle.Turtle()
pen.speed(0)
pen.width(1)

car_length = 125
car_width = car_length // 3
color = ["cyan", "blue violet", "pink", "red", "orange", "khaki", "spring green"]

def draw_car(x, y):
    draw_body(x,y)
    draw_wheels(x + (car_length / 3.5), y - (car_width / 3)) #starts with left wheel

def draw_body(x,y):
    pen.up()
    pen.setposition(x, y)
    pen.down()
    
    pen.fillcolor(random.choice(color))
    pen.begin_fill()
    for i in range(2):
        pen.forward(car_length)
        pen.left(90)
        pen.forward(car_width)
        pen.left(90)
    pen.end_fill()
    pen.up()
    
def draw_wheels(x,y):
    pen.up()
    pen.setposition(x, y)
    pen.down()
    pen.fillcolor("dark grey")
    
    pen.begin_fill()
    pen.circle(car_width/3)
    pen.end_fill()
    
    pen.up()
    pen.forward(car_width * 1.3)
    pen.down()
    
    pen.begin_fill()
    pen.circle(car_width/3)
    pen.end_fill()
    pen.up()
    
#drawing median
pen.up()
pen.setpos(-300, 0)
pen.down()


for stripes in range (10):
    pen.color("yellow")
    pen.forward(car_length // 2)
    pen.up()
    pen.forward(car_length // 4)
    pen.down()
    
pen.color("black")
turtle.onscreenclick(draw_car)
pen.hideturtle()

turtle.done()