from CircleClass import *

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
    
    center1 = (sum + root).scale(1/k4[0])
    center2 = (sum - root).scale(1/k4[0])
    center3 =  (sum + root).scale(1/k4[1])
    center4 =  (sum - root).scale(1/k4[1])
    
    return [CircleClass(k4[0],center1.a,center1.b),
            CircleClass(k4[0],center2.a,center2.b),
            CircleClass(k4[1],center3.a,center3.b),
            CircleClass(k4[1],center4.a,center4.b),]