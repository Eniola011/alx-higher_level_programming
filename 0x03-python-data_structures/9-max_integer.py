#!/usr/bin/python3
def max_integer(my_list=[]):
    list1 = len(my_list)
    if list1 == 0:
        return None
    max_list = my_list[0]
    for n in my_list:
        if n > max_list:
            max_list = n
    return max_list
