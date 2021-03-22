__author__ = 'Andrew'

class Airplane:

    def _init_(self, x, y, speed=0, size=0) :
        self._x = x
        self._y = y
        self._speed = speed
        self._size = size

    def getSpeed(self) :
        return self._speed

    def getLocation(self) :
        return self._x,self._y

    def getSize(self) :
        return self._size

    def speedUp(self,increase) :
        self._speed = self._speed + increase

    def land(self) :
        self._speed = 0
