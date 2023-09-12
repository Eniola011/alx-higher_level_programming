#!/usr/bin/python3
"""

Add Attribute Module

"""


def add_attribute(obj, name, value):
    """ Adds new attribute to an object """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    else:
        setattr(obj, name, value)
