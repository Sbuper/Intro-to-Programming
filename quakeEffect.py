__author__ = 'Andrew'

magnitude=float(input("What is the magnitude of this earth quake?"))
if magnitude >= 8 and magnitude > 7:
    print("Wow! Most structures are falling! How are we alive!?!")
elif magnitude <= 7 and magnitude > 6:
    print("Looks like most of the buildings have been destroyed....better have good insurance!")
elif magnitude <= 6 and magnitude > 4.5:
    print("Well, most buildings will be damaged, but at least nothing destroyed, right?")
elif magnitude <= 4.5:
    print("That's really not so bad, only a few buildings will be damaged, if any.")