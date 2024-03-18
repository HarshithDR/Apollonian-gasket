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