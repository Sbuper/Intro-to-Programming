__author__ = 'Sbuper'
import graphics
myColor = input("What is your favorite color")
win = graphics.GraphicsWindow(600,600)
canvas = win.canvas()

canvas.setColor(myColor)
canvas.drawRect(10,10,300,100)

win.wait()

