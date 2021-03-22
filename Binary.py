__author__ = 'Andrew'
num = int(input("Choose a number."))
finished = False

while (not finished):
 print(num%2)
 num = num//2
 if num == 0:
     finished = True