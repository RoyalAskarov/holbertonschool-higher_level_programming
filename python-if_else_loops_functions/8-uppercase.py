#!/usr/bin/python3
def uppercase(str):
    num = ord("a") - ord("A")
    str += "\n"
    for i in range(len(str)):
        if str[i].isalpha() and str[i].islower():
            print("{}".format(chr(ord(str[i]) - num)), end="")
        else:
            print("{}".format(str[i]), end="")
