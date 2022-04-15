#Author: Justin C
import turtle
turtle.bgcolor("skyblue")
turtle.setup(500,500)
pen = turtle.Turtle()
pen.pensize(4)
pen.speed(8)

#first wheel!
pen.penup()
pen.setpos(-100,0)
pen.pendown()
pen.fillcolor("yellow")
pen.begin_fill()
pen.circle(50)
pen.end_fill()

#bike body
pen.penup()
pen.setpos(-100,50)
pen.pendown()
pen.setheading(0)
pen.forward(100)
pen.left(60)
pen.forward(100)
pen.left(120)
pen.forward(100)
pen.left(60)
pen.forward(100)
pen.left(120)
pen.forward(100)
pen.left(120)
pen.forward(135)

#bike seat
pen.setheading(0)
pen.forward(20)
pen.left(180)
pen.forward(40)

#second wheel
pen.penup()
pen.setpos(100,100)
pen.pendown()
pen.fillcolor("yellow")
pen.begin_fill()
pen.circle(50)
pen.end_fill()

#handle
pen.penup()
pen.setpos(100,50)
pen.setheading(120)
pen.pendown()
pen.forward(135)
pen.left(60)
pen.forward(20)


turtle.done()