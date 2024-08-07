#!/usr/bin/python3
"""Square is a class the take int size,
great than 0.

Attributes:
    _Square__size: the size of the square.
"""


class Square:
    """Square is a class the take int size,
        great than 0.

        Attributes:
            _Square__size: the size of the square.
        Raises:
            TypeError: size must be int.
            ValueError: size must be >= zero.

    """
    def __init__(self, size=0):
        self._Square__size = size
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
