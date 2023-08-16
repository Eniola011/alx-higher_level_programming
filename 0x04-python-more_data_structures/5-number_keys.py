#!/usr/bin/python3
def number_keys(a_dictionary):
    sum_of_keys = 0
    list_of_keys = list(a_dictionary.keys())
    for key in list_of_keys:
        sum_of_keys += 1
    return sum_of_keys
