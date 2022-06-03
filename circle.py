# Class Circle
# A Circle instance accepts attribute radius (r)
# It has a method area that returns the area (A) of the circle using the
# formula A=πr2
# It has a method to calculate circumference (c) using the formula C=2πr

from asyncore import ExitNow


class Circle:
    def __init__ (self,radius):
         self.radius=radius
    def area(self):
        return 2*self.radius*22/7
    def circumference(self):
        return 2*self.radius*22.7
