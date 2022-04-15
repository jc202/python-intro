#Author: Justin C
import turtle
turtle.setup(600,600)
turtle.bgcolor("black")
pen=turtle.Turtle()
pen.speed(0)
pen.color("blue")
pen.pensize(6)

length = 60
hex_width = length * 2

pen.up()
pen.setpos(-hex_width * 2, hex_width)
pen.down()

#drawing hexagons
pen.fillcolor("yellow")

pen.begin_fill()
for i in range (6):
    pen.forward(length)
    pen.left(60)
pen.end_fill()

pen.up()
pen.setpos(-hex_width * 1.2, hex_width/2)
pen.down()

pen.begin_fill()
for i in range (6):
    pen.forward(length)
    pen.left(60)
pen.end_fill()

pen.up()
pen.setpos(-hex_width * 0.4, 0)
pen.down()

pen.begin_fill()
for i in range (6):
    pen.forward(length)
    pen.left(60)
pen.end_fill()

pen.up()
pen.setpos(hex_width * 0.4, -hex_width/2)
pen.down()

pen.begin_fill()
for i in range (6):
    pen.forward(length)
    pen.left(60)
pen.end_fill()

pen.up()
pen.setpos(hex_width * 1.2, -hex_width)
pen.down()

pen.begin_fill()
for i in range (6):
    pen.forward(length)
    pen.left(60)
pen.end_fill()


turtle.done()