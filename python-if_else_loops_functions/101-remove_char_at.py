#!/usr/bin/python3
def remove_char_at(str, n):
    strr = ""
    for i in range(len(str)):
        if i == n:
            continue
        strr += str[i]
    return strr
