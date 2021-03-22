__author__ = 'Andrew'
userInput = input("What file shall I examine?")
inputFile = open(userInput)
tempFile = 0
lst = inputFile.readline()
print(inputFile)
commentCount = 0
for X in inputFile:
        if lst[X] == "#":
            commentCount = commentCount + 1
            print(commentCount)


print("There were", commentCount,"comment lines")