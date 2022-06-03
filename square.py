# Class Square
# A Square instance accepts the attribute side (a)
# It has method area that returns the area (A) of the
# square using the formula A=a2
# It has a method to calculate the perimeter (P) of the 
# square using the formula P=4a


class Square:
    def __init__ (self,a):
        self.side=a
    def area(self):
        surfacearea=self.side**2
        return surfacearea
    def perimeter(self):
        per=4*self.side
        return per
    
