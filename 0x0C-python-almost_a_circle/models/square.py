#!/usr/bin/python3
"""

Square.py

"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """ Inherits from Rectangle class """
    def __init__(self, size, x=0, y=0, id=None):
        """ Initializes instances """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)

    def init_update(self, id=None, size=None, x=None, y=None):
        if id is not None:
            self.id = id
        if size is not None:
            self.size = size
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    def update(self, *args, **kwargs):
        if args:
            self.init_update(*args)
        elif kwargs:
            self.init_update(**kwargs)

    def to_dictionary(self):
        """ Returns the dictionary representation of a 'Square' """
        return {
            'id': self.id,
            'size': self.width,
            'x': self.x,
            'y': self.y
        }
