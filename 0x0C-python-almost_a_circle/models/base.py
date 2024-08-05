#!/usr/bin/python3
""" Module Doc"""


class Base:
    """ Class Doc"""

    __nb_objects = 0

    def __init__(self, id=None):
        self.id = id
        if self.id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
