#!/usr/bin/python3
"""

Rectangle.py

"""


from models.base import Base


class Rectangle(Base):
    """ Inherits from Base class """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ Private Instantiation
        Args:
            width: width of the rectangle
            height: height of the rectangle
            x: x
            y: y
    """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value
