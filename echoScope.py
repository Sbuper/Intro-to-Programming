__author__ = 'Andrew'

def echo(i):
    print("Echo function called with i =",i)
    if(i<1):
        return
    echo(i-1)
    print("colts",i)


echo(23)