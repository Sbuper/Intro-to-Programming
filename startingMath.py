__author__ = 'Sbuper'
import math
speed1 = float(input("what is the speed of boat 1"))
speed2 = float(input("what is the speed of boat 2"))

speedDiff = abs(speed1-speed2)
sqSpeedDiff = math.sqrt(speedDiff)

print("%2.f" %sqSpeedDiff)
