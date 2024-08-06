#!/usr/bin/python3
""" Module Doc"""


class Base:
    """ Class Doc"""
    import json

    __nb_objects = 0

    def __init__(self, id=None):
        self.id = id
        if self.id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Load string to json"""
        if list_dictionaries is None:
            return json.dumps(list())
        return json.dumps(list_dictionaries)
