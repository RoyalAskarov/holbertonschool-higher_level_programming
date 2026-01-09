#!/usr/bin/python3
"""
This module defines a Student class with attribute filtering.
"""


class Student:
    """
    Defines a student by first_name, last_name, and age.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes the student instance.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.

        If attrs is a list of strings, only attribute names contained
        in this list must be retrieved. Otherwise, all attributes
        must be retrieved.

        Args:
            attrs (list, optional): A list of strings representing the
                                   attribute names to retrieve.

        Returns:
            dict: A dictionary containing the filtered or all attributes.
        """
        if isinstance(attrs, list) and all(isinstance(a, str) for a in attrs):
            res = {}
            for item in attrs:
                if item in self.__dict__:
                    res[item] = self.__dict__[item]
            return res

        return self.__dict__
