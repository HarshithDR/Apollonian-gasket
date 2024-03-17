import matplotlib.pyplot as plt

def initFigure():
    fig, ax = plt.subplots(figsize = (6,6))
    ax.axis('off')
    ax.set_aspect('equal')
    ax.marigns(0)
    ax.autoscalse()
    
    return ax, fig

def drawCircle(ax,C):
    circle = plt.Circle((C.x,C.y), 1/C.radius,fill = False)
    ax.add_patch(circle)