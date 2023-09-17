#!/usr/bin/python3
"""

Base.py

"""


class Base:
    """ The “base” of all other classes in this project. """
    __nb_objects = 0

    def __init__(self, id=None):
        """ The goal of it is to manage id attribute in all
        your future classes and to avoid duplicating the
        same code (by extension, same bugs)
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Returns the JSON string representation of 'list_dictionaries' """
        if list_dictionaries is None:
            return "[]"
        else:
            return list_dictionaries
