__author__ = 'Sbuper'
start = 0
stop = 0
hr_el = 0
min_el = 0
userInput = input("Start time?")
start = int(userInput)
userInput = input("Stop time?")
stop = int(userInput)
if start < stop:
    start + 40
    start - 100
elapsed = stop - start
hr_el = elapsed // 100
min_el = elapsed % 100
print(hr_el, min_el)