__author__ = 'Andrew'
__author__ = 'Andrew'
import random
ppot = 20
opot = 20
dpot = 20

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
    totalval = 0
    dupeval = []
    cardlist = []

    for count in range(number):
        name, value = deck.popitem()
        temp += [name]
        card = "\n ".join(x for x in temp) + "\n "
        cardlist.append(value)
        hand_value.append(value)

    while len(hand_value) > 0:
        y = hand_value.pop(0)
        if y in hand_value:
            dupeval += [int(y)]
    count = len(dupeval) -1
    while count>= 0:
        totalval += int(dupeval[count])
        count -= 1

    return totalval, card, cardlist, temp

def opraise(pbet, opbet, ppot, opot):
    print("Your opponent has chosen to raise, the bet is now", opbet)
    if opbet <= ppot:
        betchoice = input("Will you (C)all, (R)aise or (F)old?").upper()
        while betchoice != "C" and betchoice != "R" and betchoice != "F":
            print("That input was invalid.")
            betchoice = input("Will you (C)all, (R)aise or (F)old?").upper()
    elif opbet > ppot:
        print("You have been outbet.")


    if betchoice == "C":
        pbet = opbet
    elif betchoice == "R":
        betup = input("How much will you raise by?")
        pbet += betup
    elif betchoice == "F":
        print("You chose to fold.")


def score_checker(player, dealer, opponent, community):

    if player > dealer and opponent and community:
        return "Winner!"

    elif dealer > player or opponent or community:
        return "House wins!"

    elif opponent > player or dealer or community:
        return "Opponent wins!"

    elif community > player and dealer and opponent:
        return "Community has highest! \n \n Everyone wins!"

    else:
        return "It's a tie! Crazy!!"

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

    player, plHand, plList, plhList = deal_cards(deck, 2)

    opponent, opHand, opList, ophList = deal_cards(deck, 2)

    dealer, dlHand, dlList, dlhList = deal_cards(deck, 2)

    community, comHand, comList, comhList = deal_cards(deck, 5)
    print("The flop is:\n", comHand)
    print("Each play will be given 20 chip to start. Good luck!")
    print("Pre-flop betting has now begun")
    pbet = int(input("How much will you bet?"))
    while bround1 != "end":

        if pbet <= opot and pbet <= dpot:
            betchoice = random.randrange(1,3)
            #1 = check, 2 = fold, 3 = raise
            if betchoice == 1:
                opbet = pbet
            elif betchoice == 2:
                opbet = 0
                print("Your opponenet has folded")
            elif betchoice == 3:
                opbet = round(pbet + (pbet*.5))
                opraise(pbet, opbet, ppot, opot)

    while bround2 != "end":
    while bround3 != "end":
    while bround4 != "end":

    plList2 = plList
    comList2 = comList
    plHand2 = plHand
    comHand2 = comHand
    take = "N"
    match = "N"
    count = 0
    y=0

    for x in plList2:
        if x in comList2:
            plList2.append(x)
            plHand2 += (plHand + plhList[count])
            comList2.remove(x)
            match = "Y"
    count += 1

    if match == "Y" and PlayingGame == "Y":
        take = input("Take matches from communtiy hand? (Y)es or (N)o?").upper()
        if take == "Y":
            plList = plList2
            plHand = plHand2
            print("Your new hand is:\n", plHand, "\n", "Value of this hand:", player, "\n")
        else:
            print("too bad...")
            count = 0
            for x in dlList:
                if x in comList2:
                    dlList.append(x)
                    dlHand += (dlHand + dlhList[count])
                count += 1
            count = 0
            for x in opList:
                if x in comList2:
                    opList.append(x)
                    opHand += (opHand + ophList[count])
                count += 1

    print(score_checker(player, dealer, opponent, community))
    PlayingGame = input("Continue? (Y)es or (N)o").upper()
