__author__ = 'Andrew'
from math import sqrt

num1=0
num2=0

def Pythag():
    hypo = sqrt(num1**2 + num2**2)
    print(hypo)

num1 = int(input("What is leg 1"))
num2 = int(input("What is leg 2"))

Pythag()
