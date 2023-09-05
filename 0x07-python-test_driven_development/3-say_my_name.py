#!/usr/bin/python3
"""

Say Your Name Module

"""


def say_my_name(first_name, last_name=""):
    """A function that prints your first and last name
    Args:
        parameter1: first name
        parameter2: last name
    Error:
        TypeError: if first and last name aren't strings.
    """

    if type(first_name) is not str:
        raise TypeError("first_name must be a string")

    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
