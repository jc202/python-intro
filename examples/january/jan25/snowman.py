# Create a snowman
#Author: Justin Chisholm   
import turtle
turtle.setup(750,750)
turtle.bgcolor("skyblue")
pen = turtle.Turtle()
pen.speed(0)
pen.color("black")
pen.fillcolor("white")

# ("title", "prompt", default, min, max)
drawing_size = turtle.numinput("Snowman", "Size (1, 5)", 3, 1, 5)
snowman_size = drawing_size * turtle.window_height() / 5
large_circle = snowman_size // 2
medium_circle = large_circle * 3/4
small_circle = medium_circle * 3/4


pen.color("black")
pen.fillcolor("white")

#draw medium circle
pen.up()
pen.setpos(0, -snowman_size / 2 + large_circle * 3/4)
pen.down()
pen.begin_fill()
pen.circle(medium_circle / 2)
pen.end_fill()

#draw small circle
pen.up()
pen.setpos(0, -snowman_size / 2 + large_circle * 3/4 + medium_circle * 3/4)
pen.down()
pen.begin_fill()
pen.circle(small_circle / 2)
pen.end_fill()
turtle.done()