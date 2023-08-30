#!/usr/bin/python3
"""A square class: defines a square by private instance attribute"""


class Square:
    """size is a private object attribute"""
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
    """Area of a square"""
    def area(self):
        return (self.__size ** 2)
