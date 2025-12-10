#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number % 10 == 0:
    print("Last digit of", number, "is 0 and is 0")
else:
    if number < 0:
        num = number % -10
        print("Last digit of", number, "is", num, "and is less than 6 and not 0")
    elif number > 0:
        num = number % 10
        if num > 5:
            print(f"Last digit of {number} is {num} and is greater than 5")
        else:
            print(f"Last digit of {number} is {num} and is less than 6 and not 0")
