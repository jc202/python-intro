#Author: Justin Chisholm
import turtle
turtle.setup(750,750)
turtle.bgcolor("skyblue")
pen = turtle.Turtle()
pen.speed(0)


# ("title", "prompt", default, min, max)
drawing_size = turtle.numinput("Lady Bug", "Size (1, 10)", 5, 1, 10)
wing_size = drawing_size * turtle.window_height() // 30
head_size =  wing_size // 2
spot_size = head_size // 5

#draw head
pen.up()
pen.setpos(-head_size//2,0)
pen.down()
pen.pencolor("black")
pen.fillcolor("black")
pen.begin_fill()
pen.circle(head_size)
pen.end_fill()

#draw wings
pen.up()
pen.setpos(head_size//2 + head_size , -wing_size//2)
pen.down()
pen.pencolor("black")
pen.fillcolor("red")
pen.begin_fill()
pen.circle(wing_size)
pen.end_fill()


#wing line
pen.up()
pen.pensize(5)
pen.setpos(-head_size//2, wing_size//2)
pen.down()
pen.forward(wing_size*2)

#eyes
pen.up()
pen.pensize(3)
pen.color("white")
pen.fillcolor("white")
pen.setposition(-head_size//2 - head_size/4, head_size/2)
pen.begin_fill()
pen.down()
pen.circle(spot_size)
pen.end_fill()

pen.up()
pen.setposition(-head_size//2 - head_size/4, head_size/2 + head_size/2)
pen.begin_fill()
pen.down()
pen.circle(spot_size)
pen.end_fill()
pen.up()

#spots for top wing
pen.fillcolor("black")
pen.setposition(head_size//2.5, wing_size//1.5)
pen.begin_fill()
pen.down()
pen.circle(spot_size)
pen.end_fill()
pen.up()

pen.setposition(head_size*1.5, wing_size)
pen.begin_fill()
pen.down()
pen.circle(spot_size)
pen.end_fill()
pen.up()

pen.setposition(head_size*2.75, wing_size//1.5)
pen.begin_fill()
pen.down()
pen.circle(spot_size)
pen.end_fill()
pen.up()

#bottom wing
pen.fillcolor("black")
pen.setposition(head_size//2.5, -wing_size//20)
pen.begin_fill()
pen.down()
pen.circle(spot_size)
pen.end_fill()
pen.up()

pen.setposition(head_size*1.5, -wing_size//4)
pen.begin_fill()
pen.down()
pen.circle(spot_size)
pen.end_fill()
pen.up()

pen.setposition(head_size*2.75, -wing_size//12)
pen.begin_fill()
pen.down()
pen.circle(spot_size)
pen.end_fill()
pen.up()

turtle.done()