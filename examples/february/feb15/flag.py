#Author: Justin C
import turtle
turtle.setup(800,550)
turtle.bgcolor("white")
pen = turtle.Turtle()
pen.speed(0)
pen.color("red")
pen.width(1)

x = -turtle.window_width()//2
y = -turtle.window_height()//2
stripe_width = turtle.window_width()
stripe_height = turtle.window_height()//13
#red stripes
for i in range(7):
    pen.up()
    pen.setpos(x,y)
    pen.down()
    
    #draw stripe
    pen.begin_fill()
    for i in range(4):
        if i % 2 == 0: #"if i divides evenly into two"
            pen.forward(stripe_width)
        else:
            pen.forward(stripe_height)
        pen.left(90)
    pen.end_fill()
    
    
    y += stripe_height * 2 #move up for next stripe
    
#blue rectangle
rect_width = turtle.window_width() //2
rect_height = turtle.window_height() * 6/13
x = -turtle.window_width() // 2
y = -turtle.window_height()//2 + (turtle.window_height() - rect_height)
pen.up()
pen.setpos(x,y)
pen.down()
pen.color("blue")

pen.begin_fill()
for i in range(4):
    if i % 2 == 0:
        pen.forward(rect_width)
    else:
        pen.forward(rect_height)
    pen.left(90)
pen.end_fill()

#Star Informaton
star_width = rect_width // 8
star_height = rect_height // 12
star6_padding = star_width // 2


y = -turtle.window_height()//2 + (turtle.window_height() - rect_height) + star6_padding

for row in range(6):
    x = -turtle.window_width()//2 + star6_padding // 2
    pen.up()
    pen.setpos(x,y)
    pen.down()
    
    if row % 2 == 0:
        num_stars = 6
    else:
        num_stars = 5
        x + star_width / 2 + star6_padding 
        
    for col in range(num_stars):
        x += star6_padding 
        pen.up()
        pen.setpos(x,y)
        pen.down()
        pen.color("white")
        pen.begin_fill()
        
        for i in range(5):
            pen.forward(star_width)
            pen.left(144)
            
        pen.end_fill()
        x += star_width + star6_padding 
    y += star_height *2


turtle.done()
