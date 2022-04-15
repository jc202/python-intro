#Author: Justin Chisholm
import turtle
import random
turtle.setup(600,600)
turtle.bgcolor("skyblue")
pen=turtle.Turtle()
pen.speed(0)
pen.width(3)

def get_scene():
    scene = []
    
    try:
        with open ("assignments/ass20/scene.txt") as file:
            for line in file:
                scene.append(line.strip())
    except FileNotFoundError:
        print("Sorry, your scene could not be captured.")           
    
    return scene

def draw_tree(x, y):
    pen.up()
    pen.setpos(x - 5, y - 20)
    pen.color("brown")
    pen.down()
    
    pen.begin_fill()
    for i in range(4):
        if i % 2 == 0:
           pen.forward(10)
        else:
            pen.forward(45)
        pen.right(90)
    pen.end_fill()
    
    pen.up()
    pen.setpos(x, y - 25)
    pen.color("green")
    pen.down()
    
    pen.begin_fill()
    pen.circle(circle_size * 1.25)
    pen.end_fill()
    pen.up()
    
    pen.up()
       
def draw_flower(x, y):
    pen.up()
    pen.setpos(x, y + 10)
    pen.color("green")
    pen.down()
    
    pen.setheading(-90)
    pen.forward(75)

    pen.up()
    pen.setpos(x, y)
    pen.setheading(0)
    pen.down()

    
    pen.color("red")
    for i in range(12):
        pen.circle(circle_size // 1.5)
        pen.left(90)
        pen.circle(circle_size // 1.5)
        pen.left(120)
    pen.up()

x = -turtle.window_width()// 2
y = 0
circle_size = turtle.window_width()//30

for plant in range(7):
    plant_padding = 75
    
    if plant % 2 == 0:
        x += plant_padding 
        draw_flower(x, y)
    else:
        x += plant_padding 
        draw_tree(x, y)
pen.hideturtle()
        
turtle.done()