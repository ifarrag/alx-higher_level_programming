#!/usr/bin/python3
"""Define square.
    Attribute:
        _Square__size: the size
    Return:
        size ** 2
"""


class Square:
    """Define square.
    Attribute:
        _Square__size: the size
    Return:
        size ** 2
    """
    def __init__(self, size=0):
        self._Square__size = size

    @property
    def size(self):
        return self._Square__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self._Square__size = value

    def area(self):
        """The square area."""
        return self._Square__size ** 2
