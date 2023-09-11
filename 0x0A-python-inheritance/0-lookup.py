#!/usr/bin/python3
"""

Lookup Module

"""


def lookup(obj):
    """ Returns  list of available attributes
        and methods of an object
    Args:
        obj: instance of a class
    Return:
        List of available attributes.
    """

    return dir(obj)
