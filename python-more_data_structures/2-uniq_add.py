#!/usr/bin/python3
def uniq_add(my_list=[]):
    li = []
    summ = 0
    for i in my_list:
        if i not in li:
            summ += i
            li.append(i)
    return summ

