__author__ = 'Andrew'
from airplane import Airplane

snoopy=Airplane(1,1,0,15)
redBaron=Airplane(10,10,100,15)

print(snoopy.getSpeed())
print(redBaron.getSpeed())

snoopy.speedUp(200)
print(snoopy.getSpeed())
