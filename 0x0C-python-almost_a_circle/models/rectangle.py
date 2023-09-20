#!/usr/bin/python3
"""

Rectangle Module

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
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be > 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be > 0")
        self.__y = value

    def area(self):
        """ Area of a Rectangle """
        return self.width * self.height

    def display(self):
        """ Displays a Rectangle using '#' """
        if self.height == 0 or self.width == 0:
            print("")
            return
        [print("") for y in range(self.y)]
        for hg in range(self.height):
            [print(" ", end="") for x in range(self.x)]
            [print("#", end="") for w in range(self.width)]
            print("")

    def __str__(self):
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.x, self.y,
                                                       self.width, self.height)

    def update(self, *args, **kwargs):
        if args is not None and len(args) != 0:
            attr = ['id', 'width', 'height', 'x', 'y']
            for idx in range(len(args)):
                setattr(self, attr[idx], args[idx])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ Returns the dictionary representation of a 'Rectangle' """
        attr = ['id', 'width', 'height', 'x', 'y']
        dict_key = {}

        for key in attr:
            dict_key[key] = getattr(self, key)

        return dict_key
