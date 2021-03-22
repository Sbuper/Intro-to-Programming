__author__ = 'Andrew'
num1 = int(input("Number 1?"))
num2 = int(input("Number 2?"))
num3 = int(input("Number 3?"))
fileName = input("What name do you want for the file?")
fileName = fileName + ".txt"
avg = (num1 + num2 + num3)//3

outFile = open(fileName, "w")
outFile.write("The average is ")
outFile.write(str(avg))
outFile.close()

try:
    readFile=open(fileName, "r")
except:
    print("I can't find a needle in a haystack.")
finally:
    readFile.close

stuff = readFile.readlines()
print(stuff)
readFile.close()