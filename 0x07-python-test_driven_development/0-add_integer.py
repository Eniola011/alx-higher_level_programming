#!/usr/bin/python3
"""

Addition Module

"""


def add_integer(a, b=98):
    """A function that adds two integers or floats, raise a
       "TypeError" if the two numbers aren't integers or floats
    """

    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return a + b
