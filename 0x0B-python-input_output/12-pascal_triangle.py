#!/usr/bin/python3
"""

Pascal Triangle

"""


def pascal_triangle(n):
    """ A function that eturns a list of lists of integers
        representing the Pascal’s triangle of n
    """
    if n <= 0:
        return []

    pascal = []

    for idx in range(n):
        triangle = []
        for elem in range(idx + 1):
            if elem == 0 or elem == idx:
                triangle.append(1)
            else:
                triangle.append(pascal[idx - 1][elem - 1] +
                                pascal[idx - 1][elem])
        pascal.append(triangle)

    return pascal
