__author__ = 'Andrew'

num = int(input("Hey Joe User, What's the number?"))

finished = False

while (not finished):
    print (num*num)
    done = input("Finished yet?")
    if done=="yes":
        finished=True