#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    ll = list(a_dictionary.keys())
    ll.sort()
    for key in ll:
        print(f"{key}: {a_dictionary[key]}")
