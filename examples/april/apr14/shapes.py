def draw_rectangle(pen, x, y, width, length):
    pen.up()
    pen.setpos(x,y)
    pen.down()
    
    for i in range(4):
        if i % 2 == 0:
            pen.forward(length)
        else:
            pen.forward(width)
        pen.left(90)
        
def draw_square(pen, x, y, width):
    draw_rectangle(pen, x, y, width, width)

def draw_triangle(pen, x, y, length):
    pen.up()
    pen.setpos(x,y)
    pen.down()
    
    for i in range(3):
        pen.forward(length)
        pen.left(120)