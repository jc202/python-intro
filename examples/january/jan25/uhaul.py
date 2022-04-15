#Author: Justin Chisholm   
import turtle
turtle.setup(600,600)
turtle.bgcolor("skyblue")
pen = turtle.Turtle()
pen.speed(4)
pen.color("black")
pen.fillcolor("brown")

# ("title", "prompt", default, min, max)
user_size = turtle.numinput("U-Haul", "Size (1, 10)", 5, 1, 10)
draw_size = turtle.window_width() * user_size / 4
truck_width = draw_size * .75
cab_width = draw_size - truck_width
truck_height = draw_size /2
cab_height = truck_height /2
wheel_width = draw_size *.1

# draw box
pen.up()
pen.setpos(-draw_size/2, -truck_height/2)
pen.down()
pen.fillcolor("brown")
pen.begin_fill()
pen.forward(draw_size)
pen.left(90)
pen.forward(cab_height)
pen.left(90)
pen.forward(cab_width)
pen.right(90)
pen.forward(truck_height - cab_height)
pen.left(90)
pen.forward(truck_width)
pen.left(90)
pen.forward(truck_height)
pen.end_fill()

#first wheel!
pen.up()
pen.setpos(-draw_size /3 , -truck_height/2)
pen.fillcolor("black")
pen.begin_fill()
pen.down()
pen.circle(wheel_width)
pen.up()

#second wheel
pen.left(90)
pen.forward(draw_size/2)
pen.right(90)
pen.down()
pen.circle(wheel_width)
pen.end_fill()


turtle.done()