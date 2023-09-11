#!/usr/bin/python3
"""

Isinstance Module

"""


def is_kind_of_class(obj, a_class):
    """ Is Object of a_class or a class inherited from a_class.
    Args:
        obj: object
        a_class: class
    Return: True/False
    """

    return isinstance(obj, a_class)
