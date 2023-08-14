#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    elem1 = len(tuple_a)
    elem2 = len(tuple_b)

    if elem1 == 0:
        a1 = 0
        a2 = 0
    elif elem1 == 1:
        a1 = tuple_a[0]
        a2 = 0
    else:
        a1 = tuple_a[0]
        a2 = tuple_a[1]

    if elem2 == 0:
        b1 = 0
        b2 = 0
    elif elem2 == 1:
        b1 = tuple_b[0]
        b2 = 0
    else:
        b1 = tuple_b[0]
        b2 = tuple_b[1]

    my_tuple = (a1 + b1, a2 + b2)
    return my_tuple

