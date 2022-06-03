# Class Sphere
# A Sphere Instance accepts the radius of the sphere (r)
# It has a method to calculate the surface area (A) using 
# the formula A=4πr2
# It has a method to calculate the volume (V) 
# of the sphere using the formula V = 4/3(πr3)

from cmath import pi


class Sphere:
    def __init__ (self,radius):
        self.radius=radius
    def surface_area(self):
        surfacearea=4*22/7*self.radius**2
        return surfacearea
    def calculate_volume(self):
        volume= 4/3*(22/7*self.radius**3)
        return volume 