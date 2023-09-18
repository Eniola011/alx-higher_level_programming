#!/usr/bin/python3
"""

Base.py

"""


import json
import csv
import os.path


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
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ Writes the JSON string representation of list_objs to a file """
        filename = "{}.json".format(cls.__name__)
        with open(filename, 'w') as jfile:
            if list_objs is None:
                jfile.write("[]")
            else:
                dict_list = [idx.to_dictionary() for idx in list_objs]
                jfile.write(Base.to_json_string(dict_list))

    @staticmethod
    def from_json_string(json_string):
        """ Returns the list of the JSON string representation json_string """
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)
