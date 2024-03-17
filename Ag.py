import matplotlib.pyplot as plt
from CircleClass import CircleClass
from Plot import *



if __name__ == "__main__":
    c1 = CircleClass((-1/200),200,200)
    c2 = CircleClass(1/100,100,200)
    c3 = CircleClass(1/100,300,200)

    ax, fig = initFigure()

    circle1 = plt.Circle((c1.x,c1.y),c1.radius,fill = False)
    circle2 = plt.Circle((c2.x,c2.y),c2.radius,fill = False)
    circle3 = plt.Circle((c3.x,c3.y),c3.radius,fill = False)

    ax.add_patch(circle1)
    ax.add_patch(circle2)
    ax.add_patch(circle3)

    ax.set_aspect('equal')
    ax.axis('off')
    ax.margins(0)
    ax.autoscale()
    plt.show()
    
    
    k4 