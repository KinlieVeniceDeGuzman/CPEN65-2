import math
class circle():
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return math.pi*(self.radius**2)

class circle2(circle):
    def __init__(self, diameter):
        self.diameter = diameter

    def area2(self):
        return (math.pi * (self.diameter ** 2)) / 4

while True:
    given = str(input("What is the given? If it's radius type r, if diameter type d ,if quit type q: "))
    if given.lower() == "q":
        break
    else:
        if given.lower() == "r":
            r = float(input("Radius: "))
            giv = circle(r)
            print("Area of the circle: ", round(giv.area(),2))
        else:
            d = float(input("Diameter: "))
            giv2 = circle2(d)
            print("Area of the circle: ", round(giv2.area2(),2))