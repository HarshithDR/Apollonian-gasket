import matplotlib.pyplot as plt
from CircleClass import CircleClass
from Plot import *
from descartes import *
from ComplexDescartes import *

def validate(allcircles, c):
    for other in allCircles:
        d = dist(c.center.a,c.center.b,other.center.a,other.center.b)
        if (d<0.1):
            return False
    
    if c.radius < 10: 
        return False
    

if __name__ == "__main__":
    
    iterations = 3
    ax, fig = initFigure()
    
    c1 = CircleClass((-1/200),200,200)
    c2 = CircleClass(1/100,100,200)
    c3 = CircleClass(1/100,300,200)
    allCircles = [c1,c2,c3]
    queue = [[c1,c2,c3]]
    
    for circle in allCircles:
        drawCircle(ax,circle)
    # print(12)
    
    for i in range(1,iterations):
        # print(i)
        # print(queue)
        nextQueue = []
        for triplet in queue:
            # print(type(queue))
            [c1,c2,c3] = triplet
            print('f23',type(c1))
            # print(123)
            k4 = descartes(c1,c2,c3)
            # print(k4)
            newCircles = complexDescartes(c1,c2,c3,k4)
            # print(k4)
            for ccc in newCircles:
                if validate(allCircles, ccc):
                    # print(nextQueue)
                    drawCircle(ax,ccc)
                    allCircles.append(ccc)
                    t1 = [c1, c2, ccc]
                    t2 = [c1, c3, ccc]
                    t3 = [c2, c3, ccc]
                    nextQueue.append(t1)
                    nextQueue.append(t2)
                    nextQueue.append(t3)
                    # print('next=',nextQueue)
                    # nextQueue.append(t2)
                    # nextQueue.append(t3)
        # print(queue)    
        queue = nextQueue    
    plt.show()