#!/usr/bin/python3
"""A square class"""


class Square:
    """size is a private object attribute"""
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        p = self.__size * self.__size
        return p

    """Print the character '#' according to size of square"""
    def my_print(self):
        if self.__size == 0:
            print("")
        else:
            for a in range(0, self.position[1]):
                print()
            for i in range(0, self.size):
                for b in range(0, self.position[0]):
                    print(" ", end="")
                for c in range(0, self.size):
                    print("#", end="")
                print()
