from math import pi

class Circle:
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        return  self.radius * self.radius * pi
    
radius = float(input("Enter Radius of Cirlce : "))

c1 = Circle(radius)

print("AREA = ",c1.area())
