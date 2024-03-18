import matplotlib.pyplot as plt
from CircleClass import CircleClass
from Plot import *
from descartes import *
from ComplexDescartes import *

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