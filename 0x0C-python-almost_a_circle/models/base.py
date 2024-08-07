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
        Name = cls.__name__ + ".json"
        if list_objs is not None and len(list_objs) != 0:
            list_objs = [i.to_dictionary() for i in list_objs]
        wrto = cls.to_json_string(list_objs)
        with open(Name, 'w', encoding="utf-8") as f:
            f.write(wrto)

    @staticmethod
    def from_json_string(json_string):
        import json
        if json_string is None or len(json_string) == 0:
            return list()
        return json.loads(json_string)
