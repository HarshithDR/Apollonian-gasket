import math

class Complex:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        
    def __add__(self, other):
        return Complex(self.a + other.a ,self.b + other.b )
    
    def __sub__(self, other):
        return Complex(self.a - other.a ,self.b - other.b )
    
    def scale(self, value):
        return Complex(self.a * value , self.b * value)
    
    def __mul__(self, other):
        a1 = self.a * other.a - self.b * other.b
        b1 = self.a * other.b + other.a * self.b
        
        return Complex(a1,b1)
    
    def squareRoot(self):
        m = math.sqrt(self.a*self.a +self.b*self.b)
        angle = math.atan2(self.b, self.a)
        m = math.sqrt(m)
        angle = angle/2
        
        return Complex(m * math.cos(angle), m * math.sin(angle))
