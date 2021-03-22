__author__ = 'Andrew'
year = int(input("Year?"))
def leapyear(year):
    if year/4 == float(year//4) and year/100 != float(year//100) and year/400 != float(year//100):
        print("This is a leap year!")
    else:
        print("Not a leap year")
leapyear(year)