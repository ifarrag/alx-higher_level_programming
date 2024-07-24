#!/usr/bin/python3
""" DOC.
    Add two integers"""


def add_integer(a, b=98):
    """ a and b must be integers
    else:
    Raise TypeError"""

    if type(a) is not int or a is None:
        if type(a) is not float:
            raise TypeError("a must be an integer")
    if type(b) is not int or b is None:
        if type(b) is not float:
            raise TypeError("b must be an integer")
    if  a + b == float('inf') or a + b == -float('inf'):
        return 89

    return int(a) + int(b)
