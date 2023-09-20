#!/usr/bin/python3
"""

Base Module

"""


import json
import csv


class Base:
    """ The “base” of all other classes in this project.
    Args:
        __nb_object (int): Number of instantiated Bases.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """ The goal of it is to manage id attribute in all
        your future classes and to avoid duplicating the
        same code (by extension, same bugs)
        Args:
            id (int): The identity of the new Base.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Returns the JSON string representation of 'list_dictionaries'
        Args:
            list_dictionaries (list): A list of dictionaries.
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ Writes the JSON string representation of list_objs to a file
        Args:
            list_objs (list): A list of inherited Base instances.
        """
        filename = "{}.json".format(cls.__name__)
        with open(filename, 'w') as jfile:
            if list_objs is None:
                jfile.write("[]")
            else:
                dict_list = [idx.to_dictionary() for idx in list_objs]
                jfile.write(Base.to_json_string(dict_list))

    @staticmethod
    def from_json_string(json_string):
        """ Returns the list of the JSON string representation json_string
        Args:
            json_string (str): A JSON str representation of a list of dicts.
        """
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ Returns an instance with all attributes already set
        Args:
            **dictionary (dict): Key/value pairs of attributes to initialize.
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new = cls(1, 1)
            else:
                new = cls(1)
            new.update(**dictionary)
            return new

    @classmethod
    def load_from_file(cls):
        """ Returns a list of instances """
        filename = "{}.json".format(cls.__name__)
        try:
            with open(filename, "r") as jfile:
                dict_list = Base.from_json_string(jfile.read())
                return [cls.create(**idx) for idx in dict_list]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ Save a csv file
        Args:
            list_objs (list): A list of inherited Base instances.
        """
        filename = "{}.csv".format(cls.__name__)
        with open(filename, "w", newline="") as cfile:
            if list_objs is None or list_objs == []:
                cfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(cfile, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """ Load a csv file """
        filename = "{}.csv".format(cls.__name__)
        try:
            with open(filename, "r", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    field_names = ["id", "width", "height", "x", "y"]
                else:
                    field_names = ["id", "size", "x", "y"]
                    dictlist = csv.DictReader(csvfile, fieldnames=fieldnames)
                    dictlist = [dict([k, int(v)] for k, v in d.items())
                                for d in dictlist]
                    return [cls.create(**d) for d in dictlist]
        except IOError:
            return []
