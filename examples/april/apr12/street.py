from house import House
import turtle
turtle.setup(600,600)
pen = turtle.Turtle()
pen.speed(0)
pen.pensize(2)


#my_house = House("1 A Street", 0, 0, 50, "medium aquamarine", "blue", True, True, 4)
#my_house.draw(pen)

houses = []
houses.append(House("1 A Street", -200, 0, 50, "medium aquamarine", "hot pink", True, True, 3))
houses.append(House("2 A Street", -100, 0, 50, "medium aquamarine", "red", False, True, 3))
houses.append(House("3 A Street", 0, 0, 50, "yellow", "cyan", True, False, 3))
houses.append(House("4 A Street", 100, 0, 50, "black", "tomato", False, True, 3))
houses.append(House("5 A Street", 200, 0, 50, "orange", "blue", True, True, 3))

for house in houses:
    house.draw(pen)
    
    
turtle.done()