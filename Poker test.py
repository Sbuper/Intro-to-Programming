__author__ = 'Andrew'
import random
ppot = 20
opot = 20
print("Each player will be given 20 chip to start. Good luck!", "\n")

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

deck = create_deck()

player, plHand, plList, plhList = deal_cards(deck, 2)
opponent, opHand, opList, ophList = deal_cards(deck, 2)
community, comHand, comList, comhList = deal_cards(deck, 3)

def scoring(plHand, opHand):
    print(plHand)
    print(plList)
    print("SEP")
    print(opHand)

scoring(plHand, opHand)



def score_checker(plHand, plList, opHand, opList, comHand, comList, player, opponent, community):
    plHand += comHand
    plList += comList
    plHand2 = []
    while len(plHand)>0:
        plHand2 += plHand.popitem()
        plHand2.split("of")
    player += community
    opponent+= community

    if player > opponent:
        print("You win!")
    elif player > opponent:
        print("You lose...")
    else:
        win = random.randint(1,2)
        if win == 1:
            print("You win!")
        elif win == 2:
            print("You lose...")