__author__ = 'Sbuper'
import graphics

point1 = int(input("What is X?"))
point2 = int(input("What is Y?"))
radius = int(input("What is the radius?"))
radius = radius * 2
win = graphics.GraphicsWindow(700,700)
canvas = win.canvas()

canvas.setColor("black")
canvas.drawOval(point1,point2,radius,radius)

win.wait()