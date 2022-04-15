#Author: Justin C
import turtle
turtle.setup(600,600)
turtle.bgcolor("skyblue")
pen=turtle.Turtle()
pen.speed(0)
pen.color("blue")
pen.pensize(3)

num_coordinates = int(turtle.numinput("Coordinates", "Enter Number of Coordinates: ", 6, 1))

for i in range(num_coordinates):
    pen.down()
    x = int(turtle.numinput("Shapes", "Enter the X-Coordinate: "))
    y = int(turtle.numinput("Shapes", "Enter the Y-Coordinate: "))
    pen.setpos(x,y)

    
turtle.done()