# Class Rectangle
# A Rectangle instance accepts two sides of a rectangle (w,l)
# It has method to calculate the area (A) of the rectangle using
# the formula A=wl 
# It has a method to calculate the perimeter (P)
# of the rectangle using the formula P=2(l+w)

class Rectangle:
    def __init__(self,weath,length):
        self.weath=weath
        self.length=length
    def area(self):
        return self.weath * self.length
    def perimeter(self):
        return 2*(self.length + self.weath)
