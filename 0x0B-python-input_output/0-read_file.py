#!/usr/bin/python3
"""

Read from Text File

"""


def read_file(filename=""):
    """ A function that reads a text file (UTF8)
        and prints it to stdout
    """

    with open(filename, 'r', encoding="utf-8") as file:
        read_content = file.read()
        print(read_content, end="")
