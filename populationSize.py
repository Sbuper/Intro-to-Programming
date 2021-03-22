__author__ = 'Andrew'

organismCount=int(input("How many organisms started this?"))
dailyIncrease=float(input("By what percentage, in whole numbers, did they multiply each day?"))*.01
daysMultiplying=int(input("How long has this been going on for?"))
daysLeft=1
print("Day", "    ","Approximate Population")
while daysMultiplying >= daysLeft:
    print(daysLeft, "    ",round(organismCount,6))
    organismCount=organismCount+(organismCount*dailyIncrease)
    daysLeft=daysLeft+1