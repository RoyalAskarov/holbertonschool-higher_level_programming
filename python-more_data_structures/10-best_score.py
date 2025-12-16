#!/usr/bin/python3
def best_score(a_dictionary):
    key = ""
    a = 0
    for keyy, value in a_dictionary.items():
        if value > a:
            a = value
            key = keyy
    return key
