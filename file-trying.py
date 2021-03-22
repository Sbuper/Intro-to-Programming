__author__ = 'Andrew'
try:
    newFile=open("Results.txt", "r")
except:
    print("I can't find a needle in a haystack.")
finally:
    newFile.close()