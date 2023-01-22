#circumference of circle
class circle():
    x=3.14
    def __init__(self, radius):
        self.radius=radius
    def circumference(self):
        print(2*self.x*self.radius)
circle1=circle(2)
circle1.circumference()

#volume and sureface area of circle
class volume():
    x=3.14
    h=3
    def __init__(self,radius):
        self.radius=radius
    def volume(self):
        print(self.x*self.radius**2*self.h)
        print(2*self.x*self.radius**2+2*self.x*self.radius*self.h)
volume1=volume(2)
volume1.volume()