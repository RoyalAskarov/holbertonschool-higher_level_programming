#!/usr/bin/python3
def search_replace(my_list, search, replace):
    mylist = my_list.copy()
    for i in range(len(mylist)):
        if mylist[i] == search:
            mylist[i] = replace
    return mylist