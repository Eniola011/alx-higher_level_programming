#!/usr/bin/python3
"""A MagicClass that behaves like the bytecode provided."""

import math


class MagicClass:
    def __init__(self, radius=0):
        """Initialize a magicClass.
        Args:
            radius: can be an int or a float.
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Area of magicClass"""
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """Circumference of magicClass"""
        return (2 * math.pi * self.__radius)
