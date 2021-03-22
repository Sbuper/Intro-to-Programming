__author__ = 'Andrew'

num = int(input("Pick an number"))
evennum = 0
totalnum = 0
highnum = 0
lownum = 0
avgnum = 0
finished = False
while (not finished):
   if num >= highnum:
     highnum = num
   elif num <= lownum:
     lownum = num
   elif (num%2==0):
     evennum = evennum + 1
     totalnum = totalnum + num
   elif (num%2!=0):
     totalnum = totalnum + num
   if num == 0:
    finished=True
   else: num = int(input("Pick a different number"))
   avgnum = avgnum + 1
   totalavg = totalnum // avgnum





print("The smallest number was", lownum, "whilst the largest number was", highnum,".")
print("You inputted", evennum, "even numbers.")
print("The total average of all inputs was", avgnum,".")

