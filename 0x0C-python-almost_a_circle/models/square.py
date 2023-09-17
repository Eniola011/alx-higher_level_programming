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

    def update(self, *args, **kwargs):
        if args is not None and len(args) != 0:
            attr = ['id', 'size', 'x', 'y']
            for idx in range(len(args)):
                if attr[idx] == 'size':
                    setattr(self, 'width', args[idx])
                    setattr(self, 'height', args[idx])
                else:
                    setattr(self, attr[idx], args[idx])
        else:
            for key, value in kwargs.items():
                if key == 'size':
                    setattr(self, 'width', value)
                    setattr(self, 'height', value)
                else:
                    setattr(self, key, value)
