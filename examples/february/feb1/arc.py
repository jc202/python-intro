#Author: Justin Chisholm
import turtle

turtle.bgcolor("skyblue")
turtle.setup(700,700)
pen = turtle.Turtle()
pen.speed(.5)
pen.pensize(2)
pen.color("black")
pen.fillcolor("green")
pen.hideturtle()

pen.up()
pen.setpos(-turtle.window_width()/2, 0)
pen.down()
pen.forward(turtle.window_width())
pen.up()
pen.setpos(0, -turtle.window_height()/2)
pen.down()
pen.setheading(90)
pen.forward(turtle.window_height())

arc_radius = 100

#smile
#pen.up()
#pen.setpos(-arc_radius, 0)
#pen.down()
#pen.setheading(-60)
#pen.circle(arc_radius, 120)

#frown
pen.up()
pen.setpos(arc_radius, -arc_radius)
pen.down()
pen.setheading(120)
pen.circle(arc_radius, 120)



turtle.done()