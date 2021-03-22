__author__ = 'Andrew'
gpaculm = int(input("Current GPA(single-digit only)?"))
creditcur = int(input("Current credits earned?"))
creditget = int(input("Credits currently taking?"))
targetgpa = int(input("Target cumulative GPA(single-digit only)?"))
outFile = open("GPA Info.txt", "w")

for x in range(0,8):
    if (gpaculm + x)/2 == targetgpa:
        gpaneed = x
print("You will need a GPA of", gpaneed, "this semester")
export = ("You need a gpa of", gpaneed)
outFile.write(export)
outFile.close()