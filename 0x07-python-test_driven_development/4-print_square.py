#!/usr/bin/python3
"""
Print Square Module
print square with #

"""


def print_square(size):
    """Function that prints a square with the character #.
    Args:
        size: the size length of the square
    Error:
        TypeError: If size isn't an integer
        ValueError: If size isn't less than zero
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    if not isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    for element in range(size):
        print("#" * size)
