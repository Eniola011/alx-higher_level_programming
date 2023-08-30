#!/usr/bin/python3
"""A square class"""


class Square:
    """size is a private object attribute"""
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    """Area of a square"""
    def area(self):
        return (self.__size * self.__size)

    """Print the character '#' according to size of square"""
    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for a in range(self.__size):
                for b in range(self.__size):
                    print("#", end="")
                print()
