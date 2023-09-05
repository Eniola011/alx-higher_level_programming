#!/usr/bin/python3
"""

A Text_Indentation Module

"""


def text_indentation(text):
    """Function that prints a text with 2 new lines after
    each of these characters: "., ? and :"
    Args:
        text: the inputted string
        c: delimiter
        el: element
    Error:
        TypeError: if text isn't a string
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for c in ".?:":
        text = (c + "\n\n").join([el.strip(" ") for el in text.split(c)])

    print("{}".format(text), end="")
