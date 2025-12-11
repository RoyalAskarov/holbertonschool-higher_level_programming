#!/usr/bin/python3
def fizzbuzz():
    for i in range(100):
        y = i + 1
        if y % 15 == 0:
            print("FizzBuzz", end=" ")
        elif y % 3 == 0:
            print("Fizz", end=" ")
        elif y % 5 == 0:
            print("Buzz", end=" ")
        else:
            print(y, end=" ")
