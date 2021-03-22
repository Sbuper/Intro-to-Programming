__author__ = 'Sbuper'
wSpeed = int(input("What is the current wind speed?"))
rain = input("Is it raining?")
rain = rain.upper()
if (wSpeed >= 157):
    print("There is a CAT V storm headed your way.")
    if (rain == "YES"):
      print("GET OUTTA DER'!")
elif (wSpeed >= 130):
    print("There is a CAT IV storm headed your way.")
    if (rain == "YES"):
      print("GET OUTTA DER'!")
elif (wSpeed >= 111):
    print("There is a CAT III storm headed your way.")
elif (wSpeed >= 96):
    print("There is a CAT II storm headed your way.")
elif (wSpeed >= 74):
    print("There is a CAT I storm headed your way.")
elif (wSpeed <= 74):
    print("Your good bro. No danger here.")