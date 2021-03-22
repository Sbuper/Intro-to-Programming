__author__ = 'Andrew'
import random
opot = 20
print("Use (Enter) to proceed.")
input()
chipcarry = input("Use chips from last game? (Y)es or (N)o?").upper()
while chipcarry != "Y" and chipcarry != "N":
    chipcarry = input("Use chips from last game? (Y)es or (N)o?").upper()
if chipcarry == "Y":
    potcarry = open("Bank.txt", "r")
    ppot = int(potcarry.read())
    print("You brought", ppot, "chips to the table")
else:
    print("You will have 20 chips to start.")
    ppot = 20
input()
streak = 0
finalstreak = 0
def create_deck():
    deck = { 'Ace of Spades': 1, '2 of Spades': 2, '3 of Spades': 3,
             '4 of Spades': 4, '5 of Spades': 5, '6 of Spades': 6,
             '7 of Spades': 7, '8 of Spades': 8, '9 of Spades': 9,
             '10  of Spades': 10, 'Jack of Spades': 11,
             'Queen of Spades': 12, 'King of Spades': 13,

             'Ace of Hearts': 1, '2 of Hearts': 2, '3 of Hearts': 3,
             '4 of Hearts': 4, '5 of Hearts': 5, '6 of Hearts': 6,
             '7 of Hearts': 7, '8 of Hearts': 8, '9 of Hearts': 9,
             '10  of Hearts': 10, 'Jack of Hearts': 11,
             'Queen of Hearts': 12, 'King of Hearts': 13,

             'Ace of Clubs': 1, '2 of Clubs': 2, '3 of Clubs': 3,
             '4 of Clubs': 4, '5 of Clubs': 5, '6 of Clubs': 6,
             '7 of Clubs': 7, '8 of Clubs': 8, '9 of Clubs': 9,
             '10  of Clubs': 10, 'Jack of Clubs': 11,
             'Queen of Clubs': 12, 'King of Clubs': 13,

             'Ace of Diamonds': 1, '2 of Diamonds': 2, '3 of Diamonds': 3,
             '4 of Diamonds': 4, '5 of Diamonds': 5, '6 of Diamonds': 6,
             '7 of Diamonds': 7, '8 of Diamonds': 8, '9 of Diamonds': 9,
             '10  of Diamonds': 10, 'Jack of Diamonds': 11,
             'Queen of Diamonds': 12, 'King of Diamonds': 13}

    return deck


def deal_cards(deck, number):
    hand_value = []
    temp = []
    cardlist = []

    for count in range(number):
        name, value = deck.popitem()
        temp += [name]
        card = "\n ".join(x for x in temp) + "\n "
        cardlist.append(value)
        hand_value.append(value)


    return card, cardlist, temp


def opraise(pbet, opbet, ppot):
    print("Your opponent has chosen to raise, the bet is now", opbet)
    input()
    if opbet <= ppot:
        betchoice = input("Will you (C)all, (R)aise or (F)old?").upper()
        while betchoice != "C" and betchoice != "R" and betchoice != "F":
            print("That input was invalid.")
            betchoice = input("Will you (C)all, (R)aise or (F)old?").upper()
    elif opbet > ppot:
        print("Sorry, you have been outbet.")
        global bround1
        global bround2
        global bround3
        global bround4
        bround1 = "end"
        bround2 = "end"
        bround3 = "end"
        bround4 = "end"
        betchoice = "end"


    if betchoice == "C":
        pbet = opbet
    elif betchoice == "R":
        betup = int(input("How much will you raise by?"))
        pbet += betup
    elif betchoice == "F":
        print("You chose to fold.")
        betchoice = "end"
    return pbet, opbet, betchoice


def score_checker(plhList, comhList, ophList, pot, pbet, streak, finalstreak):
    #list = nums
    #hlist = 'x of y'
    #hlist[].split = ['x','y']
    plcard1 = plhList[0].split("of")
    plcard1 = plcard1[1]
    plcard2 = plhList[1].split("of")
    plcard2 = plcard2[1]
    opcard1 = ophList[0].split("of")
    opcard1 = opcard1[1]
    opcard2 = ophList[1].split("of")
    opcard2 = opcard2[1]
    comcard1 = comhList[0].split("of")
    comcard1 = comcard1[1]
    comcard2 = comhList[1].split("of")
    comcard2 = comcard2[1]
    comcard3 = comhList[2].split("of")
    comcard3 = comcard3[1]
    comcard4 = comhList[3].split("of")
    comcard4 = comcard4[1]
    comcard5 = comhList[4].split("of")
    comcard5 = comcard5[1]
    player = 0
    opponent = 0

    if plcard1 == plcard2:
        player = 2
    elif plcard1 == plcard2 and plcard1 == comcard1:
        player = 3
    elif plcard1 == plcard2 and plcard1 == comcard2:
        player = 3
    elif plcard1 == plcard2 and plcard1 == comcard3:
        player = 3
    elif plcard1 == plcard2 and plcard1 == comcard4:
        player = 3
    elif plcard1 == plcard2 and plcard1 == comcard5:
        player = 3
    elif plcard1 == plcard2 and plcard1 == comcard1 and comcard1 == comcard2:
        player = 4
    elif plcard1 == plcard2 and plcard1 == comcard1 and plcard1 == comcard2 and plcard1 == comcard3:
        player = 5
    elif plcard1 == plcard2 and plcard1 == comcard2:
        player = 3
    elif plcard1 == plcard2 and plcard1 == comcard2 and plcard1 == comcard3:
        player = 4
    elif plcard1 == plcard2 and plcard1 == comcard2 and plcard1 == comcard3 and plcard1 == comcard4:
        player = 5
    elif plcard1 == plcard2 and plcard1 == comcard3:
        player = 3
    elif plcard1 == plcard2 and plcard1 == comcard3 and plcard1 == comcard4:
        player = 4
    elif plcard1 == plcard2 and plcard1 == comcard3 and plcard1 == comcard4 and plcard1 == comcard5:
        player = 5
    elif plcard1 == plcard2 and plcard1 == comcard4:
        player = 3
    elif plcard1 == plcard2 and plcard1 == comcard4 and plcard1 == comcard5:
        player = 4

    #Opponent scoring
    elif opcard1 == opcard2:
        opponent = 2
    elif opcard1 == opcard2 and opcard1 == comcard1:
        opponent = 3
    elif opcard1 == opcard2 and opcard1 == comcard2:
        opponent = 3
    elif opcard1 == opcard2 and opcard1 == comcard3:
        opponent = 3
    elif opcard1 == opcard2 and opcard1 == comcard4:
        opponent = 3
    elif opcard1 == opcard2 and opcard1 == comcard5:
        opponent = 3
    elif opcard1 == opcard2 and opcard1 == comcard1 and comcard1 == comcard2:
        opponent = 4
    elif opcard1 == opcard2 and opcard1 == comcard1 and opcard1 == comcard2 and opcard1 == comcard3:
        opponent = 5
    elif opcard1 == opcard2 and opcard1 == comcard2:
        opponent = 3
    elif opcard1 == opcard2 and opcard1 == comcard2 and opcard1 == comcard3:
        opponent = 4
    elif opcard1 == opcard2 and opcard1 == comcard2 and opcard1 == comcard3 and opcard1 == comcard4:
        opponent = 5
    elif opcard1 == opcard2 and opcard1 == comcard3:
        opponent = 3
    elif opcard1 == opcard2 and opcard1 == comcard3 and opcard1 == comcard4:
        opponent = 4
    elif opcard1 == opcard2 and opcard1 == comcard3 and opcard1 == comcard4 and opcard1 == comcard5:
        opponent = 5
    elif opcard1 == opcard2 and opcard1 == comcard4:
        opponent = 3
    elif opcard1 == opcard2 and opcard1 == comcard4 and opcard1 == comcard5:
        opponent = 4

    if player > opponent:
        print("You win!")
        pot += int(pbet*.7//2)
        streak += 1
    elif player < opponent:
        print("You lose...")
        pot -= pbet
        if finalstreak < streak:
            finalstreak = streak
            streak = 0
        elif finalstreak > streak:
            streak = 0
    elif player == opponent:
        print("Tie!")
    else:
        #In case of error, victory is random
        winrand = random.randrange(1,3)
        if winrand ==2:
            print("You win!")
            pot += int(pbet*.7//2)
            streak += 1
        else:
            print("You lose...")
            pot -= pbet
            if finalstreak < streak:
                finalstreak = streak
                streak = 0
            elif finalstreak > streak:
                streak = 0

    return pot, streak, finalstreak



PlayingGame = "Y"
pldealt = "N"
flop = "N"
river = "Y"
turn = "Y"
deck = create_deck()
pot = 0

while PlayingGame == "Y":
    if 5 > len(deck):
        print("Re-shuffling...\n")
        deck = create_deck()
    bround1 = "start"
    bround2 = "start"
    bround3 = "start"
    bround4 = "start"

    plHand, plList, plhList = deal_cards(deck, 2)

    opHand, opList, ophList = deal_cards(deck, 2)

    comHand, comList, comhList = deal_cards(deck, 3)


    while bround1 != "end":
        print("Your Hand is:\n", plHand)
        print("Pre-flop betting has now begun", "\n")
        print("You have", ppot, "chips.")
        pbet = int(input("How much will you bet?"))
        if pbet <= opot:
            betchoice = random.randrange(1,6)
            #1 = check, 2 = fold, 3 = raise
            if betchoice <= 3:
                opbet = pbet
                print("Your opponent chose to call.")
                input()
                bround1 = "end"
            elif betchoice >= 4:
                opbet = round(pbet + (pbet*.5))
                pbet, opbet, betchoice = opraise(pbet, opbet, ppot)
                bround1 = "end"
        elif pbet > opot:
            opbet = 0
            print("Your opponent chose to fold.")
            input()
            bround1 = "end"
            bround2 = "end"
            bround3 = "end"
            bround4 = "end"


    while bround2 != "end":
        print("Your Hand is:\n", plHand)
        print("The flop is:\n", comHand)
        print("The bet is currently at", pbet,".")
        praise = input("Will you raise? (Y)es or (N)o?").upper()
        while praise == "Y":
            pbet2 = pbet + int(input("How much would you like to raise by?"))
            if pbet2 <= ppot:
                pbet = pbet2
                praise = "N"
            elif pbet2 > ppot:
                print("You do not have that many chips.")
                input()
                praise = input("Will you raise? (Y)es or (N)o?")
        if pbet <= opot:
            betchoice = random.randrange(1,6)
            #1 = check, 2 = fold, 3 = raise
            if betchoice <= 3:
                opbet = pbet
                print("Your opponent chose to call.")
                input()
                bround2 = "end"
            elif betchoice >= 4:
                opbet = round(pbet + (pbet*.5))
                pbet, opbet, betchoice = opraise(pbet, opbet, ppot)
                bround2 = "end"
        elif pbet > opot:
            opbet = 0
            print("Your opponent chose to fold.")
            input()
            bround2 = "end"
            bround3 = "end"
            bround4 = "end"


    while bround3 != "end":
        comHand2, comList2, comhList2 = deal_cards(deck, 1)
        comHand += comHand2
        comList += comList2
        comhList += comhList2
        print("Your Hand is:\n", plHand)
        print("The turn is", comHand2)
        input()
        print("Totally community hand:", "\n", comHand)
        input()
        print("The bet is currently at", pbet,".")
        praise = input("Will you raise? (Y)es or (N)o?").upper()
        while praise == "Y":
            pbet2 = pbet + int(input("How much would you like to raise by?"))
            if pbet2 <= ppot:
                pbet = pbet2
                praise = "N"
            elif pbet2 > ppot:
                print("You do not have that many chips.")
                input()
                praise = input("Will you raise? (Y)es or (N)o?")
        if pbet <= opot:
            betchoice = random.randrange(1,6)
            #1 = check, 2 = fold, 3 = raise
            if betchoice <= 3:
                opbet = pbet
                print("Your opponent chose to call.")
                input()
                bround3 = "end"
            elif betchoice >= 4:
                opbet = round(pbet + (pbet*.5))
                pbet, opbet, betchoice = opraise(pbet, opbet, ppot)
                bround3 = "end"

        elif pbet > opot:
            opbet = 0
            print("Your opponent chose to fold.")
            input()
            bround3 = "end"
            bround4 = "end"

    while bround4 != "end":
        comHand2, comList2, comhList2 = deal_cards(deck, 1)
        comHand += comHand2
        comList += comList2
        comhList += comhList2
        print("Your Hand is:\n", plHand)
        print("The river is", comHand2)
        input()
        print("Totally community hand:", "\n", comHand)
        input()
        print("The bet is currently at", pbet,".")
        praise = input("Will you raise? (Y)es or (N)o?").upper()
        while praise == "Y":
            pbet2 = pbet + int(input("How much would you like to raise by?"))
            if pbet2 <= ppot:
                pbet = pbet2
                praise = "N"
            elif pbet2 > ppot:
                print("You do not have that many chips.")
                input()
                praise = input("Will you raise? (Y)es or (N)o?")
        if pbet <= opot:
            betchoice = random.randrange(1,6)
            #1 = check, 2 = fold, 3 = raise
            if betchoice <= 3:
                opbet = pbet
                print("Your opponent chose to call.")
                input()
                bround4 = "end"
            elif betchoice >= 4:
                opbet = round(pbet + (pbet*.5))
                pbet, opbet, betchoice = opraise(pbet, opbet, ppot)
                bround4 = "end"
        elif pbet > opot:
            opbet = 0
            print("Your opponent chose to fold.")
            input()
            bround4 = "end"

    pot, streak, finalstreak = score_checker(plhList, comhList, ophList, pot, pbet, streak, finalstreak)
    input()
    PlayingGame = input("Continue? (Y)es or (N)o").upper()

if PlayingGame == "N":
    save = input("Would you like to save your longest streak? (Y)es or (N)o?").upper()
    while save != "Y" and save != "N":
        save = input("Would you like to save your longest streak? (Y)es or (N)o?").upper()
    if save == "Y":
        try:
            f = open("High Scores.txt")
            f.close()
        except IOError as e:
            outFile = open("High Scores.txt", "w")
        name = input("Enter initals:")
        outFile = open("High Scores.txt", "r")
        test = outFile.read()
        if test == "":
            outFile = open("High Scores.txt", "w")
            score = ("Scores:\n" + name + " - " + str(finalstreak))
            print("2")
            outFile.write(score)
        elif test != "":
            score = (test + "\n" + name + " - " + str(finalstreak))
            print("1")
            outFile = open("High Scores.txt", "w")
            outFile.write(score)
            outFile.close()
    carry = input("Would you like to carry you chips over to your next game? (Y)es or (N)o?").upper()
    while carry != "Y" and carry != "N":
        carry = input("Would you like to carry you chips over to your next game? (Y)es or (N)o?").upper()
    if carry == "Y":
        outFile2 = open("Bank.txt", "w")
        outFile2.write(str(pot))
        outFile2.close()


# Credit Jackson Cooper for lines 396 & 399