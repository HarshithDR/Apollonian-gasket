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
    allCircles = complexDescartes(c1,c2,c3,k4)

    drawCircle(ax,allCircles[0])
    drawCircle(ax,allCircles[1])
    drawCircle(ax,allCircles[2])
    drawCircle(ax,allCircles[3])
    
    plt.show()