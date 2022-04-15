# Author: Justin C
import turtle
turtle.setup(600,600)
turtle.bgcolor("skyblue")
pen=turtle.Turtle()
pen.speed(0)
pen.color("black")

pen.up()
pen.setpos(100,100)
pen.down()

trunk_width = turtle.window_width() // 10
lg_triangle = trunk_width * 3
md_triangle = lg_triangle * 3/4
sm_triangle = md_triangle * 3/4
star_width = sm_triangle / 2
bottom_y = -lg_triangle * 3/2

pen.up()
pen.setpos(-trunk_width / 2, bottom_y)
pen.down()

#draw trunk
pen.color("brown")
pen.begin_fill()
for i in range(4):
    pen.forward(trunk_width)
    pen.left(90)
pen.end_fill()

pen.up()
pen.setpos(-lg_triangle / 2, bottom_y + trunk_width)
pen.down()
pen.color("dark green")

#draw large triangle
pen.fillcolor("dark green")
pen.begin_fill()
for i in range (3):
    pen.forward(lg_triangle)
    pen.left(120)
pen.end_fill()

#draw md triangle
pen.up()
pen.setpos(-md_triangle / 2, bottom_y + trunk_width + lg_triangle/2)
pen.down()

pen.fillcolor("dark green")
pen.begin_fill()
for i in range (3):
    pen.forward(md_triangle)
    pen.left(120)
pen.end_fill()

#small tri
pen.up()
pen.setpos(-sm_triangle / 2, bottom_y + trunk_width + lg_triangle/2 + md_triangle/2)
pen.down()

pen.fillcolor("dark green")
pen.begin_fill()
for i in range (3):
    pen.forward(sm_triangle)
    pen.left(120)
pen.end_fill()

#draw star
pen.up()
pen.setpos(-star_width / 2, bottom_y + trunk_width + lg_triangle/2 + md_triangle/2 + sm_triangle + star_width /2)
pen.down()

pen.color("yellow")
pen.fillcolor("yellow")
pen.begin_fill()
for i in range (3):
    pen.forward(star_width)
    pen.left(120)
pen.end_fill()

pen.up()
pen.setpos(-star_width / 2, bottom_y + trunk_width + lg_triangle/2 + md_triangle/2 + sm_triangle * .8 + star_width /2)
pen.down()

pen.begin_fill()
for i in range (3):
    pen.forward(star_width)
    pen.right(120)
pen.end_fill()

turtle.done()