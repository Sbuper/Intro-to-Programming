__author__ = 'Andrew'

def highThree(num1, num2, num3):
    highest = num1
    if num2>num1:
        highest = num2
        if num3>num2:
            highest = num3
    elif num3>num1:
        highest = num3
    return highest

num1 = int(input("What's number 1"))
num2 = int(input("What's number 2"))
num3 = int(input("What's number 3"))

high=highThree(num1, num2, num3)
print(high)