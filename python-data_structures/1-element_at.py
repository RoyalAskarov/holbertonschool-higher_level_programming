#!/usr/bin/python3
def element_at(my_list, idx):
    n = len(my_list)
    if idx >= n or idx < 0:
        return None
    return my_list[idx]
