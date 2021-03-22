__author__ = 'Andrew'
larry = 0
moe = 0
curly = 0

state = input("Who won the election for California?").upper()
if state == "LARRY":
    larry += 55
elif state == "MOE":
    moe += 55
elif state == "CURLY":
    curly += 55
state = input("Florida?").upper()
if state == "LARRY":
    larry += 29
elif state == "MOE":
    moe += 29
elif state == "CURLY":
    curly += 29
state = input("Illinois?").upper()
if state == "LARRY":
    larry += 20
elif state == "MOE":
    moe += 20
elif state == "CURLY":
    curly += 20
state = input("NY?").upper()
if state == "LARRY":
    larry += 29
elif state == "MOE":
    moe +=  29
elif state == "CURLY":
    curly += 29
state = input("Ohio?").upper()
if state == "LARRY":
    larry += 18
elif state == "MOE":
    moe += 18
elif state == "CURLY":
    curly += 18
state = input("Texas?").upper()
if state == "LARRY":
    larry += 38
elif state == "MOE":
    moe += 38
elif state == "CURLY":
    curly += 38

if moe > larry and moe > curly:
    print("Winner, and new president is Moe with", moe, "Electoral Votes")
elif larry > moe and larry > curly:
    print("Winner, and new president is Larry with", larry, "Electoral Votes")
elif curly > larry and curly > moe:
    print("Winner, and new president is Curly with", curly, "Electoral Votes")