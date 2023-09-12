#!/usr/bin/python3
"""

MyInt Module

"""


class MyInt(int):
    """ Inherits from int
    """
    def __eq__(self, other):
        """ checks for inequality """
        return int.__ne__(self, other)

    def __ne__(self, other):
        """ checks for equality """
        return int.__eq__(self, other)
