#!/usr/bin/python3
""" Square is special Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Class Doc"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(self, size, size, x, y, id)

    def area(self):
        """ get the area 2*size"""
        Rectangle.area()

    def __str__(self):
        return "[Square] (" + str(self.id) + ") "\
                + str(self.x) + "/" + str(self.y)\
                + " - " + str(self.width)