#!/usr/bin/python3
"""
The Square class with size
raise Error if size not int or less than 0. 

"""


class Square:
""" Args: size
Attributes: _Square__size
raise Error if size not int or less than 0 """
    def __init__(self, __size = 0):
        self._Square__size = __size
    if type(__size) != int:
        raise TypeError("size must be an integer")
    if self._Square__size < 0:
        raise ValueError("size must be >= 0")
