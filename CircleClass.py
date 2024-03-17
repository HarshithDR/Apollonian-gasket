class CircleClass: 
    def __init__(self,bend,x,y):
        self.x = x
        self.y = y
        self.bend = bend
        self.radius = abs(1/self.bend)
