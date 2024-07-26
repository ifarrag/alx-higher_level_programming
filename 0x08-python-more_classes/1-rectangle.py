#!/usr/bin/python3
"""Rectangle.
    define a Rectangle"""


class Rectangle:
    """ Define Rectangle """
    def __init__(self, width=0, height=0):
        self._Rectangle__height = height
        self._Rectangle__width = width

    @property
    def width(self):
        return self._Rectangle__width

    @property
    def height(self):
        return self._Rectangle__height

    @height.setter
    def height(self, value):
        if value is None:
            raise TypeError("height must be an integer")
        if type(value) is not int and type(value) is not float:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
    
    @width.setter
    def width(self, value):
        if value is None:
            raise TypeError("width must be an integer")
        if type(value) is not int and type(value) is not float:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
