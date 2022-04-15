#Author: Justin C
import turtle

turtle.bgcolor("white")
turtle.setup(500,500)
pen = turtle.Turtle()

pen.speed(.5)
pen.pensize(15)
books = turtle.numinput("Reading Log", "How many books have you read this month:")
style= ("Arial", 45, "normal")

#draw circle
arc_radius = turtle.window_width()/4

pen.up()
pen.setpos(0, -arc_radius)
pen.down()
pen.setheading(0)

#design the 
if books >=30:
    pen.color("dark goldenrod")
    pen.fillcolor("khaki")
    pen.begin_fill()
    pen.circle(arc_radius)
    pen.end_fill()
    turtle.up()
    turtle.setpos(-arc_radius/3,-arc_radius/4)
    turtle.color("dark goldenrod")
    turtle.write("$10", font = style)
elif books >=15:
    pen.color("slate gray")
    pen.fillcolor("light grey")
    pen.begin_fill()
    pen.circle(arc_radius)
    pen.end_fill()
    turtle.up()
    turtle.setpos(-arc_radius/3,-arc_radius/4)
    turtle.color("slate gray")
    turtle.write("$5", font = style)
elif books >= 5:
    pen.color("brown")
    pen.fillcolor("chocolate")
    pen.begin_fill()
    pen.circle(arc_radius)
    pen.end_fill()
    turtle.up()
    turtle.setpos(-arc_radius/3,-arc_radius/4)
    turtle.color("brown")
    turtle.write("$2", font = style)
else:
    pen.color("red")
    pen.circle(arc_radius)
    turtle.up()
    turtle.setpos(-arc_radius/3,-arc_radius/4)
    turtle.color("red")
    turtle.write("$0", font = style)


turtle.done()