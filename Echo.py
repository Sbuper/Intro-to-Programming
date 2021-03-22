__author__ = 'Andrew'

val1="a"
val2=0
def Echome():
    print(val1*val2)
    Echome()

val1 = input("Input 1?")
val2 = int(input("Input 2?"))

Echome()