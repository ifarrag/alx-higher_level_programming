#!/usr/bin/python3
""" Square is special Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Class Doc"""
    def __init__(self, size, x=0, y=0, id=None):
        self.__size = size
        super().__init__(self.__size, self.__size, x, y, id)

    @property
    def size(self):
        return self.__size
    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__size = value

    def __str__(self):
        return "[Square] (" + str(self.id) + ") "\
                + str(self.x) + "/" + str(self.y)\
                + " - " + str(self.width)
