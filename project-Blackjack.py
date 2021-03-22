__author__ = 'Andrew'
print("Use (Enter) to proceed.")
input()
chipcarry = input("Use chips from last game? (Y)es or (N)o?").upper()
while chipcarry != "Y" and chipcarry != "N":
    chipcarry = input("Use chips from last game? (Y)es or (N)o?").upper()
if chipcarry == "Y":
    potcarry = open("Bank.txt", "r")
    pot = int(potcarry.read())
    print("You brought", pot, "chips to the table")
else:
    print("You will have 20 chips to start.")
    pot = 20
input()
finalstreak = 0
streak = 0
okay = "N"
def create_deck():
    deck = { 'Ace of Spades': 1, '2 of Spades': 2, '3 of Spades': 3,
             '4 of Spades': 4, '5 of Spades': 5, '6 of Spades': 6,
             '7 of Spades': 7, '8 of Spades': 8, '9 of Spades': 9,
             '10  of Spades': 10, 'Jack of Spades': 10,
             'Queen of Spades': 10, 'King of Spades': 10,

             'Ace of Hearts': 1, '2 of Hearts': 2, '3 of Hearts': 3,
             '4 of Hearts': 4, '5 of Hearts': 5, '6 of Hearts': 6,
             '7 of Hearts': 7, '8 of Hearts': 8, '9 of Hearts': 9,
             '10  of Hearts': 10, 'Jack of Hearts': 10,
             'Queen of Hearts': 10, 'King of Hearts': 10,

             'Ace of Clubs': 1, '2 of Clubs': 2, '3 of Clubs': 3,
             '4 of Clubs': 4, '5 of Clubs': 5, '6 of Clubs': 6,
             '7 of Clubs': 7, '8 of Clubs': 8, '9 of Clubs': 9,
             '10  of Clubs': 10, 'Jack of Clubs': 10,
             'Queen of Clubs': 10, 'King of Clubs': 10,

             'Ace of Diamonds': 1, '2 of Diamonds': 2, '3 of Diamonds': 3,
             '4 of Diamonds': 4, '5 of Diamonds': 5, '6 of Diamonds': 6,
             '7 of Diamonds': 7, '8 of Diamonds': 8, '9 of Diamonds': 9,
             '10  of Diamonds': 10, 'Jack of Diamonds': 10,
             'Queen of Diamonds': 10, 'King of Diamonds': 10}

    return deck


def deal_cards(deck, number):
    hand_value = 0
    temp = []

    for count in range(number):
        name, value = deck.popitem()
        temp += [name]
        card = "\n ".join(x for x in temp) + "\n "
        hand_value += value

    return hand_value, card

def score_checker(player, dealer, opponent, streak, finalstreak, bet, pot):
    if opponent > 21:
        opponentfinal = ("a bust")
        opponent = 0
    elif opponent <= 21:
        opponentfinal = opponent
    if dealer > 21:
        dealerfinal = ("a bust")
        dealer = 0
    elif dealer <= 21:
        dealerfinal = dealer
    print(" Your score was", player)
    input()
    print(" Your opponent had", opponentfinal)
    input()
    print(" The dealer had", dealerfinal)
    input()
    if dealer and opponent > 21:
        streak += 1
        pot += int(bet*.7//1)+1
        print("Winner!")


    elif player > dealer and player > opponent:
        streak += 1
        pot += int(bet*.7//1)+1
        print("Winner!")


    elif player < dealer or player < opponent:
        print("Sorry, you lose!")
        pot -= bet
        if finalstreak < streak:
            finalstreak = streak
            streak = 0
        elif finalstreak > streak:
            streak = 0


    elif player == dealer or player == opponent:
        print("It's a tie!")

    return streak, finalstreak, pot
PlayingGame = "Y"
deck = create_deck()

while PlayingGame == "Y":
    print("You have", pot, "chips remaining.")
    while okay != "Y":
        try:
            bet = int(input("How much will you bet?"))
            while bet > pot or bet < 0.5:
                print("You don't have that many chips!")
                input()
                bet = int(input("How much will you bet2?"))
            okay = "Y"
        except:
            print("That's not a number!")
    okay = "N"
    playerschoice = "undefined"
    done = "no"
    if 1 > len(deck):
        print(" Re-shuffling...\n")
        deck = create_deck()

    player, plHand = deal_cards(deck, 2)
    print(" Your hand is:\n", plHand, "\n", "Value of this hand:", player, "\n")
    opponent, opHand = deal_cards(deck, 2)
    dealer, dlHand = deal_cards(deck, 2)
    temp = dlHand.split("\n")
    print(" The dealer has a \n", temp[0])

    while player <= 21 and playerschoice != "STAND":
        playerschoice = input("(S)tand or (H)it?").upper()
        if playerschoice == "S":
            streak, finalstreak, pot = score_checker(player, dealer, opponent, streak, finalstreak, bet, pot)
            player = 22
            done = "y"

        elif playerschoice == "H":
            player2, plHand2 = deal_cards(deck, 1)
            player += player2
            plHand += plHand2
            if opponent < 17:
                opponent2, opHand2 = deal_cards(deck, 1)
                opponent += opponent2
                opHand += opHand2
            if dealer < 17:
                dealer2, dlHand2 = deal_cards(deck, 1)
                dealer += dealer2
                dlHand += dlHand2
            print("\n", " Your hand is:\n", plHand, "\n", "Value of this hand:", player, "\n")
        elif playerschoice != "h" or "s":
            playerschoice = input("Please make a valid choice...")

    if player > 21 and done != "y":
        print(" Sorry, that's a bust!")

    print("\n")
    print("You have", pot, "chips.")
    input()
    PlayingGame = input(" Continue? (Y)es or (N)o").upper()
    while PlayingGame != "Y" and PlayingGame != "N":
        print(" That's not a valid answer.")
        PlayingGame = input(" Continue? (Y)es or (N)o").upper()

if PlayingGame == "N":
    save = input("Would you like to save your longest streak? (Y)es or (N)o?").upper()
    while save != "Y" and save != "N":
        save = input("Would you like to save your longest streak? (Y)es or (N)o?").upper()
    if save == "Y":
        try:
            f = open("High Scores.txt", "r")
            f.close()
        except IOError as e:
            outFile = open("High Scores.txt", "w")
        name = input("Enter initals:")
        outFile = open("High Scores.txt", "r")
        test = outFile.read()
        if test == "":
            outFile = open("High Scores.txt", "w")
            score = ("Scores:\n" + name + " - " + str(finalstreak))
            outFile.write(score)
        elif test != "":
            score = (test + "\n" + name + " - " + str(finalstreak))
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


# Credit Jackson Cooper for lines 107, 114, 169 & 172, see Citations