#!/usr/bin/python3
""" Square is special Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Class Doc"""
    def __init__(self, size, x=0, y=0, id=None):
        self.__width = size
        self.__height = size
        super().__init__()

    def __str__(self):
        return "[Square] (" + str(self.id) +") "\
                str(self.__x) + "/" + str(self.___y) + " - " + str(self.__width)
