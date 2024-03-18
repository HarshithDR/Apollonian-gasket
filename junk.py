# import matplotlib.pyplot as plt

# fig, ax = plt.subplots()

# c = (0.5,0.5)
# r = 0.3

# circle = plt.Circle(c,r,fill = False)
# ax.add_patch(circle)
# ax.set_aspect('equal')
# ax.axis('off')
# plt.show()


# import matplotlib.pyplot as plt

# class Circle:
#     def __init__(self, bend, x, y):
#         self.x = x
#         self.y = y
#         self.bend = bend
#         self.radius = abs(1 / self.bend)

# c1 = Circle(-1/200, 200, 200)
# c2 = Circle(1/100, 100, 200)
# c3 = Circle(1/100, 300, 200)

# def initFigure():
#     fig, ax = plt.subplots(figsize=(6, 6))
#     ax.axis('off')
#     ax.set_aspect('equal')
#     ax.margins(0)
#     ax.autoscale()
    
#     return fig, ax

# def drawCircle(ax, C):
#     circle = plt.Circle((C.x, C.y), C.radius, fill=False)
#     ax.add_patch(circle)

# fig, ax = initFigure()

# drawCircle(ax, c1)
# drawCircle(ax, c2)
# drawCircle(ax, c3)

# plt.show()



