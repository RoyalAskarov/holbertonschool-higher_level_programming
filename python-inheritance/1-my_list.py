#!/usr/bin/python3
"""
This module defines the MyList class which inherits from list.
"""


class MyList(list):
    """
    A class that inherits from the built-in list class.
    """

    def print_sorted(self):
        """
        Prints the list elements in ascending sorted order.
        All elements are assumed to be of type int.
        """
        print(sorted(self))
