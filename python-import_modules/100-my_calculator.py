#!/usr/bin/python3
import sys
from calculator_1.py import add, sub, mul, div
if __name__ == "__main__":
    n = len(sys.argv)
    if n != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        print(1)
    elif sys.argv[2] not in ['+', '-', '*', '/']:
        print("Unknown operator. Available operators: +, -, * and /")
        print(1)
    else:
        if sys.argv[2] == '+':
            print("{} + {} = {}".format(sys.argv[1], sys.argv[3], int(sys.argv[1]) + int(sys.argv[2])))
        elif sys.argv[2] == '-':
            print("{} - {} = {}".format(sys.argv[1], sys.argv[3], int(sys.argv[1]) - int(sys.argv[2])))
        elif sys.argv[2] == '*':
            print("{} * {} = {}".format(sys.argv[1], sys.argv[3], int(sys.argv[1]) * int(sys.argv[2])))
        else:
            print("{} / {} = {}".format(sys.argv[1], sys.argv[3], int(sys.argv[1]) / int(sys.argv[2])))
