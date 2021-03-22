__author__ = 'Andrew'

def announce_authur(your_name):
    print("Hello ")
    print("I am Arthur,")
    print("King of the Britons")

def get_name():
    name=input("By what name should the King address you?")
    return (name)

#Start of main program

your_name=get_name()
announce_authur(your_name)
print(your_name)