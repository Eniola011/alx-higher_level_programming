#!/usr/bin/python3
"""

Same-Class Module

"""


def is_same_class(obj, a_class):
    """ if the object is exactly an instance of the specified class
    Args:
        obj: object
        a_class: class
    Return:
        True: if obj is an instance of class
        False: if obj is not an instance of class
    """

    return True if type(obj) is a_class else False
