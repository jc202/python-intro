class House:
    def __init__(self, address, x, y, width, building_color, roof_color, chimney, double_doors, num_windows):
        self.address = address
        self.x = x
        self.y = y
        self.width = width
        self.building_color = building_color
        self.roof_color = roof_color
        self.chimney = chimney
        self.double_doors = double_doors
        self.num_windows = num_windows
    
    def draw(self, pen):
        self.set_pos(self.x - self.width//2, self.y - self.width//2, pen)
        self.draw_base(pen)
        self.draw_chimney(pen)
        self.draw_roof(pen)
        self.draw_address(pen)

    
    def draw_address(self, pen):
        self.set_pos(self.x - self.width * .7, self.y - self.width * 1.1, pen)
        style = ("Arial", int(self.width / 5), "bold")
        pen.write(self.address, font = style)

    
    def draw_chimney(self, pen):
        if self.chimney == False:
            return #get out of function so you don't draw a chimney
        
        self.set_pos(self.x + self.width * .2, self.y + self.width * .7, pen)
        pen.color(self.building_color)
        pen.begin_fill()
        for i in range(4):
            if i % 2 == 0:
                pen.forward(self.width * .2)
            else:
                pen.forward(self.width * .6)
            pen.left(90)
        pen.end_fill()
            
    def draw_roof(self, pen):
        self.set_pos(self.x - self.width // 1.5, self.y + self.width // 2, pen)
        pen.color(self.roof_color)
        pen.begin_fill()
        for i in range(3):
            pen.forward(self.width * 1.25)
            pen.left(120)
        pen.end_fill()        
        
    def draw_base(self, pen):
        pen.color(self.building_color)
        pen.begin_fill()
        for i in range(4):
            pen.forward(self.width)
            pen.left(90)
        pen.end_fill()
        
    def set_pos(self, x, y, pen):
        pen.up()
        pen.setpos(x, y)
        pen.down()