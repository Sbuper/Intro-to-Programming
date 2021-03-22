__author__ = 'Andrew'
f = open("Preamble.txt")
fout = open("My Favorite Song.txt", "w")
lst = f.readlines()
for x in lst:
    fout.write(x)
    fout.close
