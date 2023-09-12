#!/usr/bin/python3
"""

Square Module

"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Inherits from Rectangle
    """

    def __init__(self, size):
        """ Initialize private instance """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        return super().__str__()

    def area(self):
        """ Area of a Square """
        return self.__size ** 2
