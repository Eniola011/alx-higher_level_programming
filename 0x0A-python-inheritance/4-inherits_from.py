#!/usr/bin/python3
"""

Inherited Module

"""


def inherits_from(obj, a_class):
    """ Is object an instance of a class that inherited
        (directly or indirectly) from the specified class
    Args:
        obj: object
        a_class: class
    Return: True/False
    """

    return isinstance(obj, a_class) and type(obj) != a_class
