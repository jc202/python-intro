#Author: Justin Chisholm
import turtle
import random
turtle.setup(600,600)
turtle.bgcolor("white")
pen=turtle.Turtle()
pen.speed(3)
pen.width(3)
pen.color("black")

color = ["cyan", "blue violet", "khaki", "spring green"]

def draw_tri(x, y, width, color):
    pen.fillcolor(color)
    pen.up()
    pen.setpos(x,y)
    pen.down()
    
    pen.begin_fill()
    for i in range(3):
        pen.forward(width)
        pen.left(120)
    pen.end_fill()

def draw_art_cube(x, y, size, color):

    for cube in range(20):
        for i in range(2):
            draw_tri(x, y, size, random.choice(color))
            pen.left(60)
            break
        
x = random.randint(-turtle.window_width()//2, turtle.window_width()//2)
y = random.randint(-turtle.window_height()//2, turtle.window_height()//2)
draw_art_cube(x, y, 40, color)

turtle.done()