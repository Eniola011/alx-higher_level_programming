#!/usr/bin/python3
def remove_char_at(str, n):
    strng = ""
    for a in range(len(str)):
        if a != n:
            strng += str[a]
    return strng
