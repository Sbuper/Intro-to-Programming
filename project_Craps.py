__author__ = 'Andrew'
import random
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
okay = "N"
finished = "No"
streak = 0
finalstreak = 0
def game(roll):
    gameover = "False"
    count=2
    while gameover != "True":
        roll2 = random.randrange(1,7) + random.randrange(1,7)
        if roll2 == 7:
            gameover = "True"
            winner = "D"
            loser = "P"
            print("Roll", count, "was", roll2)
            count+=1
            input()
        elif roll2 == roll:
            gameover = "True"
            winner = "P"
            loser = "D"
            print("Roll", count, "was", roll2)
            input()
            print("That's a match!")
            count+=1
        elif roll2 != roll and roll2 != 7:
            print("Roll", count, "was", roll2)
            count+=1
            input()

    return winner, loser

def potcalc(pot, bet, winner, choice, roll, streak, finalstreak):
    if roll == 4 or 10:
        payoff = 2
    elif roll == 5 or 9:
        payoff = .5
    elif roll == 6 or 8:
        payoff = .2
    else:
        payoff = 2

    if winner == choice:
        pot += bet*payoff
        print("Hurray! You win!")
        streak +=1
    elif winner == "N" and choice == "D":
        pot = bet
    elif winner != choice and winner !="N":
        pot = pot - bet
        print("Sorry, you lose!")
        if finalstreak < streak:
            finalstreak = streak
            streak = 0
        elif finalstreak > streak:
            streak = 0
    return pot, streak, finalstreak


while finished != "N":
    roll = random.randrange(1,7) + random.randrange(1,7)
    print("You have", pot, "chips remaining.")
    input()
    betchoice=input("Choose your bet: (P)ass or (D)on't Pass?").upper()
    while betchoice != "P" and betchoice != "D":
        print("That wasn't an option.")
        betchoice=input("Choose your bet: (P)ass or (D)on't Pass?").upper()
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
    print("The roll is", roll)
    input()
    if roll == 2 or roll ==3:
        crapout = "True"
        print("The roll crapped out.")
        input()
        winner = "D"
        loser = "P"
    elif roll == 7 or roll == 11:
        crapnatural = "True"
        print("The roll was a natural roll.")
        input()
        winner = "P"
        loser = "D"
    elif roll == 12:
        print("The roll crapped out.")
        input()
        winner = "N"
        loser = "P"
    else:
        print(roll,"is the point number.")
        input()
        winner, loser = game(roll)
    pot, streak, finalstreak = potcalc(pot, bet, winner, betchoice, roll, streak, finalstreak)
    print("You have", pot, "chips.")
    input()
    finished = input("Continue? (Yes) or (N)o?").upper()
    while finished != "Y" and finished != "N":
        finished = input("Continue? (Yes) or (N)o?").upper()

if finished == "N":
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


# Credit Jackson Cooper for lines 83, 90, 128 & 131, see Citations