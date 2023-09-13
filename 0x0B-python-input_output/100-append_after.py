#!/usr/bin/python3
"""

Append-After to Text File

"""


def append_after(filename="", search_string="", new_string=""):
    """ A function that inserts a line of text to a file, after
        each line containing a specific string
    """
    with open(filename, 'r', encoding="utf-8") as file:
        content = file.readlines()

    with open(filename, 'w', encoding="utf-8") as file2:
        strng = ""
        for line in content:
            strng += line
            if search_string in line:
                strng += new_string
        file2.write(strng)
