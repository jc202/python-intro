#Author: Justin C
import turtle

turtle.bgcolor("skyblue")
turtle.setup(500,500)
pen = turtle.Turtle()
pen.pensize(4)
pen.speed(.5)
pen.color("black")
style = ("Arial", 12, "normal")

#draw thermometer 
t_height = 400
t_width = t_height/4
pen.up()
pen.setpos(-t_width/2, -t_height/2)
pen.down()
pen.forward(t_width)
pen.left(90)
pen.forward(t_height)
pen.up()
pen.left(90)
pen.forward(t_width)
pen.down()
pen.left(90)
pen.forward(t_height)

#setup thermometer markings
turtle.up()
turtle.setpos(t_width/2 + 20, -t_height/2)
turtle.down()
turtle.write("0%", font = style)

#marking = 25%
turtle.up()
turtle.setpos(t_width/2 + 20, -t_height/4)
turtle.down()
turtle.write("25%", font = style)

#marking = 50%
turtle.up()
turtle.setpos(t_width/2 + 20, 0)
turtle.down()
turtle.write("50%", font = style)

#marking = 75%
turtle.up()
turtle.setpos(t_width/2 + 20, t_height/4)
turtle.down()
turtle.write("75%", font = style)

#marking = 100%
turtle.up()
turtle.setpos(t_width/2 + 20, t_height/2)
turtle.down()
turtle.write("100%", font = style)

#get donations
donations = turtle.numinput("Donations", "Enter total donations:")
goal = 10000
percent_goal = donations/goal 

#error case corrections (donations neg or larger than goal)
if percent_goal < 0:
    percent_goal = 0
elif percent_goal > 1:
    percent_goal = 1

#drawing thermometer
d_height = t_height * percent_goal #d_height means donation height
pen.up()
pen.setpos(-t_width/2, -t_height/2)
pen.down()
pen.fillcolor("red")
pen.begin_fill()
pen.setheading(0)
pen.forward(t_width)
pen.left(90)
pen.forward(d_height)
pen.left(90)
pen.forward(t_width)
pen.left(90)
pen.forward(d_height)
pen.end_fill()

#if reached goal say nice thing
if percent_goal >= 1:
    turtle.up()
    turtle.setpos(-t_width/2, t_height/2 + 20)
    turtle.down()
    turtle.write("Goal Achieved", font = style)


turtle.done()