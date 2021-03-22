__author__ = 'Sbuper'
__author__ = 'Sbuper'
import graphics
userColor = input("Color?")
color1 = "black"
color2 = "black"
win = graphics.GraphicsWindow(600,600)
canvas = win.canvas()

if len("userColor")%2 ==0:
     color1 = userColor
else :
    color2 = userColor

canvas.setColor(color2)
canvas.drawOval(100,100,400,400)

canvas.setColor(color1)
canvas.drawOval(150,150,300,300)

canvas.setColor(color2)
canvas.drawOval(175,175,250,250)

win.wait()
