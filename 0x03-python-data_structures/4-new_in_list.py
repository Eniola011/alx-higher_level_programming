#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    copy_list = my_list[:]
    len_list = len(my_list) - 1
    if idx < 0 or idx > len_list:
        return my_list
    else:
        copy_list = my_list[:]
        copy_list[idx] = element
        return copy_list
