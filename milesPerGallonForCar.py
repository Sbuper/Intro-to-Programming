__author__ = 'Sbuper'
mpg = 0.0
miles = 0.0
gas = 0.0
float(mpg)
float(miles)
float(gas)
userInput = input("How many miles?")
miles = int(userInput)
userInput = input("How many gallons?")
gas = int(userInput)
("%2.2f" % miles)
("%2.2f" % gas)
("%2.2f" % mpg)
mpg = miles / gas
print(mpg)
print("You get")
print("%2.2f" % mpg)
print("miles per gallon.")
