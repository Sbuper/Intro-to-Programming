__author__ = 'Andrew'
from horse import Horse

horse1=Horse()
horse2=Horse()
horse3=Horse()

horse1.reset()
horse2.reset()
horse3.reset()
horse1.advance()
horse1.advance()
horse2.advance()
horse1.slow_down()

result1=horse1.getValue()
print("Steps for horse1:", result1)

result2=horse2.getValue()
print("Steps for horse1:", result2)

result3=horse3.getValue()
print("Steps for horse1:", result3)