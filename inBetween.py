__author__ = 'Andrew'

def inBetween(low, high):
    validNum=int(input("Gimme a number bro"))
    while validNum<low or validNum>high:
        print("You have been chastized. Try again.")
        validNum=int(input("Try again!"))
    if validNum<high and validNum>low:
        print("Your number is valid")
    return validNum

inBetween(10,20)