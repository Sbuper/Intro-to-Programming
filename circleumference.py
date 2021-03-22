__author__ = 'Andrew'
import math

num=0
def circ():
    surf = (4*math.pi)*(num**2)
    print(surf)

num = int(input("What is the radius?"))

circ()
