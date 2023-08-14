#!/usr/bin/python3
def no_c(my_string):
    strng = ""
    for char in my_string:
        if char != 'c' and char != 'C':
            strng += char
    return strng
