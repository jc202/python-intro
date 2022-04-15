#Author: Justin C
import turtle
import random
turtle.setup(800,600)
turtle.bgcolor("skyblue")
pen = turtle.Turtle()
pen.speed(0)
pen.width(1)

grid_size = int(turtle.numinput("Size", "Enter Size: ", 5, 1, 10))
tree_sq_width= turtle.window_width()//grid_size 
trunk_width = tree_sq_width // 5
padding = (tree_sq_width - trunk_width)// 2
tree_trunk_height = trunk_width * 2.5
leaf_radius = trunk_width

x = -turtle.window_width()//2 + padding
y = -turtle.window_height()//2 + padding //2

for row in range(grid_size):
    x = -turtle.window_width()//2 + padding
    
    for row in range(grid_size):
        pen.up()
        pen.setpos(x,y)
        pen.down()
        pen.color("brown")
        
        pen.begin_fill()
        #trunk
        for i in range(4):
            if i % 2 == 0:
                pen.forward(trunk_width)
            else:
                pen.forward(tree_trunk_height)
            pen.left(90)
        pen.end_fill()
        
        pen.up()
        pen.setpos(x + trunk_width //2, y + tree_trunk_height * .8)
        pen.down()
        
        #leaves
        pen.color("green")
        pen.begin_fill()
        pen.circle(leaf_radius)
        pen.end_fill()
        x += tree_sq_width
    y += tree_sq_width





turtle.done()