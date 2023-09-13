#!/usr/bin/python3
"""

Object from a “JSON file”

"""


import json


def load_from_json_file(filename):
    """ A function that creates an Object from a “JSON file”
    """

    with open(filename, 'r', encoding="utf-8") as file:
        return json.load(file)
