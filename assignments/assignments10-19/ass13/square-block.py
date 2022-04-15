#Author: Justin C
import turtle
turtle.setup(600,600)
turtle.bgcolor("skyblue")
pen=turtle.Turtle()
pen.speed(0)
pen.color("black")
pen.pensize(3)

rows = int(turtle.numinput("Block", "Enter Number of Rows: ", 5, 1))
colors = []
sq_size = turtle.window_height() // (rows * 2)
row_size = turtle.window_width() // 2
y = -row_size  / 2

pen.up()
for i in range(rows):
    color = turtle.textinput("Block", "Enter color of row: ")
    colors.append(color)
    x = -row_size / 2
    
    pen.begin_fill()
    pen.setpos(x,y)
    pen.down()
    pen.fillcolor(color)
    
    while x != row_size / 2:
        pen.begin_fill()
        for num_squares in range (4):
            pen.forward(sq_size)
            pen.left(90)
        pen.end_fill()
        pen.forward(sq_size)
        x += sq_size
    pen.up()
    y += sq_size
    
turtle.done()