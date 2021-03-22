__author__ = 'Andrew'
import graphics

num = int(input("Pick a number."))

win = graphics.GraphicsWindow(1000,700)
canvas = win.canvas()

canvas.setFill("red")
canvas.setOutline("green")

for y in range(0,num,1):
 for x in range(0,y+1,1):
   canvas.drawRect(x*50,y*50,50,50)


win.wait()