__author__ = 'Andrew'
f = open("peas.txt")
fout = open("peas2.txt", "w")
lst = f.readlines()
lst.reverse()
for x in lst:
    fout.write(x)
    fout.close