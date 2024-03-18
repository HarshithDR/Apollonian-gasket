from complex import *

class CircleClass: 
    def __init__(self,bend,x,y):
        self.center = Complex(x,y)
        self.bend = bend
        self.radius = abs(1/self.bend)
