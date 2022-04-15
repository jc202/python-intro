#Author: Justin Chisholm
import turtle
import random
turtle.setup(600,600)
turtle.bgcolor("white")
pen=turtle.Turtle()
pen.speed(0)
pen.width(2)
pen.color("black")

face_radius = 30

def draw_face(x, y):
    draw_head(x,y)
    draw_eye(x - face_radius *.4, y) #left eye
    draw_eye(x + face_radius *.4, y) #right eye
    draw_mouth(x, y - face_radius *.5)
    
    
def draw_head(x,y):
    set_pos(x, y - face_radius)
    pen.fillcolor("yellow")
    pen.begin_fill()
    pen.circle(face_radius)
    pen.end_fill()
    

def draw_eye(x,y):
    eye_radius = face_radius / 5
    set_pos(x, y - eye_radius)
    pen.fillcolor("black")
    pen.begin_fill()
    
    if random.randint(0, 1) == 0:
        pen.begin_fill()
        pen.circle(eye_radius)
        pen.end_fill()
    else:
        set_pos(x - eye_radius, y)
        pen.forward(eye_radius *2)

def draw_mouth(x,y):
    mouth_radius = face_radius *.5
    
    if random.randint(0,1) == 0:
        set_pos(x - mouth_radius * .8, y)
        pen.fillcolor("black")
        pen.setheading(-60)
        pen.circle(mouth_radius, 120)
        pen.setheading(0)
    else:
        set_pos(x, y - mouth_radius/2)
        pen.fillcolor("grey")
        pen.begin_fill()
        pen.circle(mouth_radius/2)
        pen.end_fill()
    
def set_pos(x, y):
    pen.up()
    pen.setpos(x,y)
    pen.down()
    
turtle.onscreenclick(draw_face)
pen.hideturtle()

turtle.done()