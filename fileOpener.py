__author__ = 'Andrew'
f = open("peas.txt")
line = f.readline()
while line:
    line = line.rstrip()
    print(line.swapcase())
    line = f.readline()

f.close()