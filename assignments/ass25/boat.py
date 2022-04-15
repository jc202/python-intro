class Boat:
    def __init__(self, x, y, main_color, width):
        self.x = x
        self.y = y
        self.main_color = main_color
        self.width = width
    
    def draw(self, pen):
        self.set_pos(self.x, self.y, pen)
        pen.setheading(0)
        self.draw_frame(pen)
        self.draw_pole(pen)
        self.draw_flag(pen)
        
    def draw_frame(self, pen):
        pen.color("black")
        pen.fillcolor(self.main_color)
        #pen starting from top left 
        pen.begin_fill()
        pen.forward(self.width)
        pen.right(120)
        pen.forward(self.width // 4)                        
        pen.right(60)
        pen.forward(self.width // 1.3)
        pen.right(60)
        pen.forward(self.width // 4)  
        pen.end_fill()

    def draw_pole(self, pen):
        pen.color("brown")
        self.set_pos(self.x + self.width//2, self.y, pen)
        pen.setheading(90)
        pen.forward(self.width//2)
    
    def draw_flag(self, pen):
        pen.color("black")
        pen.fillcolor(self.main_color)
        pen.setheading(210)
        pen.begin_fill()
        for i in range(3):
            pen.forward(self.width//4)
            pen.left(120)
        pen.end_fill()
    
    def set_pos(self, x, y, pen):
        pen.up()
        pen.setpos(x, y)
        pen.down()

