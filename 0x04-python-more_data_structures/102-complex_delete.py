#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    list_of_keys = list(a_dictionary.keys())
    for keyvalue in list_of_keys:
        if value == a_dictionary.get(keyvalue):
            del a_dictionary[keyvalue]
    return a_dictionary
