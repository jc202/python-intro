#Author: Justin C
import turtle
import random
turtle.setup(600,600)
turtle.bgcolor("black")
pen = turtle.Turtle()
pen.speed(0)

style = ("Arial", 12, "bold")

#we'll beach variables for the ocean as well!
beach_height = turtle.window_height() // 4 
sign_height = beach_height // 2
beach_width = turtle.window_width() // 2
sign_width = beach_width // 2.5


#drawing the beach
pen.color("khaki")
pen.fillcolor("khaki")

pen.up()
pen.setpos(-beach_width, -beach_height)
pen.down()

pen.begin_fill()
for i in range(4):
    pen.forward(beach_width)
    pen.right(90)
pen.end_fill()
pen.up()

#drawing water
pen.color("blue")
pen.fillcolor("blue")
pen.setpos(0, -beach_height)
pen.down()

pen.begin_fill()
pen.circle(-beach_height)
for i in range(4):
    pen.forward(beach_width)
    pen.right(90)
pen.end_fill()
pen.up()

#Sign on the beach
pen.setpos(-turtle.window_width() // 2.5, -beach_height)
pen.color("black")
pen.fillcolor("brown")
pen.down()

pen.begin_fill()
for i in range(2):
    pen.forward(sign_width)
    pen.left(90)
    pen.forward(sign_height)
    pen.left(90)
pen.end_fill()
pen.forward(sign_width//2)
pen.right(90)
pen.forward(sign_width)
pen.hideturtle()

#letters for sign
turtle.pencolor("gold")
turtle.penup()
turtle.setpos(-turtle.window_width() // 2.6, -beach_height // 1.25)
turtle.pendown()
turtle.write("Starlit Shores", font = style)


#stars!
colors = []
num_stars = int(turtle.numinput("Stars", "Number of Stars: ", 5, 1, 10, ))
star_width = turtle.window_width() // (num_stars * 4.5)
pen.setheading(0)
x = -turtle.window_width() // 2.5
for star in range (num_stars):
    star_name = turtle.textinput("Star Name", "Name Your Star: ")
    color = turtle.textinput("Star Color", "Color Your Star: ")
    colors.append(color)
    pen.color(color)
    turtle.color(color)
    y = random.randint(-turtle.window_height()//-7, turtle.window_height()//3)
    
    pen.up()
    pen.setpos(x,y)
    pen.down()
    
    #draw top triangle
    pen.begin_fill()
    for i in range(3):
        pen.forward(star_width)
        pen.left(120)
    pen.end_fill()
    
    pen.up()
    pen.setpos(x, y + (star_width / 2))
    pen.down()
    
    #bottom triangle
    pen.begin_fill()
    for i in range(3):
        pen.forward(star_width)
        pen.left(-120)
    pen.end_fill()

    turtle.penup()
    turtle.setpos(x,y + star_width)
    turtle.pendown()
    turtle.write(star_name, font = style)
    
    x += star_width * 4.5
turtle.done()