#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    set_a = set(set_1)
    set_b = set(set_2)
    return (set_a ^ set_b)
