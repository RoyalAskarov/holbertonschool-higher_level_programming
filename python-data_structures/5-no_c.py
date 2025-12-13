#!/usr/bin/python3
def no_c(my_string):
    strr = ""
    for i in my_string:
        if i.lower() != 'c':
            strr += i
    return strr
