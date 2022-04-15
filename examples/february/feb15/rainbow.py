#Author: Justin C
import turtle
turtle.setup(600,600)
turtle.bgcolor("sky blue")
pen = turtle.Turtle()
pen.speed(0)
pen.color("black")
pen.width(20)

colors = ("violet", "indigo", "blue", "green", "yellow", "orange", "red")
radius = turtle.window_width()//6
y = 0

for color in colors:
    pen.up()
    pen.setpos(0,y)
    pen.down()
    pen.color(color)
    pen.setheading(60)
    pen.circle(-radius, 120)
    y+=20
    



turtle.done()