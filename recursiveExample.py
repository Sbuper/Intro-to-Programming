__author__ = 'Andrew'

def star_echo(superstar,echoNum):
    if(echoNum<1):
        return
    star_echo(superstar,echoNum-1)
    print(superstar,"is-a number",echoNum)

star_echo("Mario",100)