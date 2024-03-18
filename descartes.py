import math

def descartes(c1,c2,c3):
    k1 = c1.bend
    k2 = c2.bend
    k3 = c3.bend
    
    sum = k1 + k2 + k3
    root = 2 * math.sqrt(k1*k2 +k2*k3 +k1*k3)
    
    return [sum + root, sum - root]