#!/usr/bin/python3
"""
This module provides a function to generate Pascal's Triangle.
"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing Pascal's triangle.

    Args:
        n (int): The number of rows of Pascal's triangle to generate.

    Returns:
        list: A list of lists of integers, or an empty list if n <= 0.
    """
    if n <= 0:
        return []

    triangle = [[1]]

    while len(triangle) < n:
        prev_row = triangle[-1]
        # Start every row with 1
        new_row = [1]

        # Calculate values by summing adjacent elements from the previous row
        for i in range(len(prev_row) - 1):
            new_row.append(prev_row[i] + prev_row[i + 1])

        # End every row with 1
        new_row.append(1)
        triangle.append(new_row)

    return triangle
