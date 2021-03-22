__author__ = 'Andrew'
good = "Nope!"
goody = "Nope!"
while good != "K":
    try:
        num1 = int(input("Pick a number, any number..."))
        good = "K"

    except:
        good = "Nay!"

while goody != "K":
    try:
        num2 = int(input("What will you divide it by?..."))
        goody = "K"
    except:
        goody = "Nay!"
numDivided = num1 / num2
print(numDivided)