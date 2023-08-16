#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    my_dict = list(a_dictionary.keys())
    my_dict.sort()
    for key in my_dict:
        print("{}: {}".format(key, a_dictionary.get(key)))
