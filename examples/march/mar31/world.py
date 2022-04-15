import turtle
import random
turtle.setup(600,600)
turtle.bgcolor("medium slate blue")
pen = turtle.Turtle()
pen.speed(0)
pen.width(1)
pen.color("black")
pen.hideturtle()

def get_colors():
    colors = []

    try:
        with open ("examples/mar24/colors.txt") as file:
            for line in file:
                colors.append(line.strip())

    except FileNotFoundError:
        print("Sorry, your color file doesn't exist.")
        
    return colors

def draw_color_strip(y, height, color):
    x = -int(turtle.window_width()/2)

    pen.up()
    pen.setpos(x,y)
    pen.down()
    
    pen.color(color)
    pen.begin_fill()
    for i in range(4):

        if i % 2 == 0:
            pen.forward(turtle.window_width())
        else:
            pen.forward(height)
        pen.left(90)
    pen.end_fill()

def save_colors(color): 
    try:
        with open ("examples/mar24/colors.txt", "w") as file:
            for color in colors:
                file.write(color + "\n")
    except FileNotFoundError:
        print("Sorry, your color file doesn't exist.")
        
        
def change_color(x,y):
    user_color = turtle.textinput("Colors", "Enter color: ").strip() 
    stripe_height = turtle.window_height()/len(colors)
    section = y // stripe_height

    index = int(-section + (len(colors) - 1)//2)
    colors[index] = user_color
    draw_color_strip(section * stripe_height, stripe_height, user_color)
    save_colors(colors)
    

#main program
colors = get_colors()
height = int(turtle.window_height()/len(colors))
y = turtle.window_height()//2

for color in colors:
    y -= height
    draw_color_strip(y,height, color)


turtle.onscreenclick(change_color)

turtle.done()