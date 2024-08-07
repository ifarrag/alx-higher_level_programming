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

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Load string to json"""
        import json
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        dmp = json.dumps(list_dictionaries)
        return dmp

    @classmethod
    def save_to_file(cls, list_objs):
        fName = str(cls.__name__) + ".json"
        wr_to = to_json_string(list_objs)
        with open(fName, 'w', encoding="utf-8") as f:
            f.write(wr_to)
