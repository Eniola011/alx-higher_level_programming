#!/usr/bin/python3
"""

Student Module

"""


class Student:
    """ Defines a Student """

    def __init__(self, first_name, last_name, age):
        """ Instantiation of Public Attributes """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ Retrieves a dictionary representation of a Student instance """
        obj = self.__dict__.copy()
        if type(attrs) is list:
            for elem in attrs:
                if type(elem) is not str:
                    return obj

            dict_list = {}

            for i in range(len(attrs)):
                for j in obj:
                    if attrs[i] == j:
                        dict_list[j] = obj[j]
            return dict_list

        return obj

    def reload_from_json(self, json):
        """ Replaces all attributes of the Student instance """
        for elem in json:
            self.__dict__[elem] = json[elem]
