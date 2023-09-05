#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
ldig = abs(number) % 10
if number < 0:
    ldig = ldig * -1
print("last digit of {} is {} and is ".format(number, ldig), end="")
if ldig == 0:
    print("0")
elif ldig > 5:
    print("greater than 5")
else:
    print("less than 6 and not 0")
