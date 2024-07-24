#!/usr/bin/python3
""" DOC.
    Add two integers"""


def add_integer(a, b=98):
    """ a and b must be integers
    else:
    Raise TypeError"""

    if a is None or type(a) is not int:
        if type(a) is not float:
            raise TypeError("a must be an integer")
    if b is None or type(b) is not int:
        if type(b) is not float:
            raise TypeError("b must be an integer")

    return int(a) + int(b)
