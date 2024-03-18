import matplotlib.pyplot as plt
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

class CircleClass: 
    def __init__(self,bend,x,y):
        self.center = Complex(x,y)
        self.bend = bend
        self.radius = abs(1/self.bend)

def initFigure():
    fig, ax = plt.subplots(figsize = (6,6))
    ax.axis('off')
    ax.set_aspect('equal')
    ax.margins(0)
    ax.autoscale()
    
    return ax, fig

def drawCircle(ax,C):
    circle = plt.Circle((C.center.a,C.center.b), C.radius,fill = False)
    ax.add_patch(circle)

def descartes(c1,c2,c3):
    k1 = c1.bend
    k2 = c2.bend
    k3 = c3.bend
    
    sum = k1 + k2 + k3
    root = 2 * math.sqrt(k1*k2 +k2*k3 +k1*k3)
    
    return [sum + root, sum - root]

def complexDescartes(c1,c2,c3,k4):
    k1 = c1.bend
    k2 = c2.bend
    k3 = c3.bend
    z1 = c1.center
    z2 = c2.center
    z3 = c3.center
    
    sum = z1.scale(k1) + z2.scale(k2) + z3.scale(k3)
    root_sum = ((z1 *z2).scale(k1 *k2) + 
            (z2 *z3).scale(k2 *k3) + (z1 *z3).scale(k1 *k3))
    root = root_sum.squareRoot().scale(2)
    
    return [(sum + root).scale(1/k4) , (sum - root).scale(1/k4)]

    
if __name__ == "__main__":
    c1 = CircleClass((-1/200),200,200)
    c2 = CircleClass(1/100,100,200)
    c3 = CircleClass(1/100,300,200)

    ax, fig = initFigure()

    drawCircle(ax,c1)
    drawCircle(ax,c2)
    drawCircle(ax,c3)

    k4 = descartes(c1,c2,c3)
    # r4 = abs(1/k4[0])
    z4 = complexDescartes(c1,c2,c3,k4[0])
    # print(z4[0].a)
    c4 = CircleClass(k4[0], z4[0].a, z4[0].b)
    
    drawCircle(ax,c4)
    
    # c4 = CircleClass(k4[1], z4[0].a, z4[0].b)
    # drawCircle(ax,c4)
    plt.show()