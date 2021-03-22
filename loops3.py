__author__ = 'Andrew'
import graphics

numCircles = int(input("User, how many circles?"))
win = graphics.GraphicsWindow(1000,1000)
canvas = win.canvas()
for y in range (0,16,1):
   for x in range(1, numCircles,1):
    if (x%2==0):
       canvas.setColor("green")
    else: canvas.setColor("red")
    canvas.drawRect(x*50,y*50,50,50)

win.wait()
