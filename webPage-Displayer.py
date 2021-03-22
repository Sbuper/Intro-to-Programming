__author__ = 'Andrew'
from urllib.request import urlopen

address = "https://floridapolytechnic.org/"
webPage = urlopen(address)
encoding = "utf-8"
# This part reads/prints the contents of the webpage
for line in webPage :
    print(line)
# This part copies it into an HTML file
newHTML = open("Thingy.HTML", "w")
for line in webPage :
    newHTML.write(str(line))
    newHTML.close

dumpedCode = webPage.readlines()


webPage.close()
