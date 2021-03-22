__author__ = 'Andrew'
import math
inFile = open("fairbanks.txt", "r")
test2 = {}
count = 0
count2 = 0
avg = 0
avg2 = 0
for line in inFile:
    test = inFile.readline().rstrip()
    if test != "":
        count += 1
        day = ("day-" + str(count))
        test2[day] = (float(test))
        avg = avg + abs(float(test))

    avg = avg / count
while count2 < len(test2):
    for x in range(1,16):
        day2 = "day-" + str(x)
        avg2 += abs(test2[day])
        count2 += 1

print(test2)
print(avg)
print(avg2)
