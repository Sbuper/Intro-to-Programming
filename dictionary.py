__author__ = 'Andrew'
roomDict = {"CS101":3004 , "CS102":4501 , "CS103":6755 , "NT110":1244 , "CM241":1411}
userSearch = input("What course are you taking next year?").upper()
print("Your class is in room",roomDict[userSearch])