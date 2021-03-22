__author__ = 'Andrew'
inFile = open("Tom Hanks.txt", "r")
outFile = open("movies.txt", "w")
movieDictionary = {}

userInput = input("Which year? No characters or symbols please.")
userInput = userInput.replace(" ", "")

title = inFile.readline().rstrip()
while title != "":
    year = inFile.readline().rstrip()
    role = inFile.readline().rstrip()
    roleTitle = title + "\nStarred as " + role
    if year in movieDictionary:
        temp = movieDictionary[year] + "\n \n" + title + "\nStarred as " + role
        movieDictionary[year] = temp
    else:
        movieDictionary[year] = roleTitle
    title = inFile.readline().rstrip()

if userInput in movieDictionary:
    print(movieDictionary[userInput])
    outFile.write(movieDictionary[userInput])
else:
    print("Sorry, try again.")