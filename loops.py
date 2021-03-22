__author__ = 'Andrew'

birth = int(input("What year did you first spawn?"))

while ((birth<1972) |(birth>2000)):
    if (birth<1972):
        print("How you still breathing man?")
    else: print("Get back in the daycare sonny!")
birth = int(input("You are invalid! What year did you REALLY first spawn?"))