#!/usr/bin/python3
"""

Rectangle Module

"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ A class that inherits
    """
    def __init__(self, width, height):
        """ Initialize private instance """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
