#!/usr/bin/python3
num = ord('z')
for i in range(26):
    if i % 2 == 1:
        print("{}".format(chr(num-i).upper()), end="")
    else:
        print("{}".format(chr(num-i)), end="")
