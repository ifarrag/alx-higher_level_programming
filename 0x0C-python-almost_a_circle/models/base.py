#!/usr/bin/python3
""" Module Doc"""


class Base:
    """ Class Doc"""

    __nb_objects = 0

    import json
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

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == "Rectangle":
            r = cls(1, 1, 0, 0, 1)
        else:
            r = cls(1, 0, 0, 1)
        r.update(**dictionary)
        return r

    @classmethod
    def load_from_file(cls):
        if cls.__name__ == "Rectangle":
            with open("Rectangle.json", encoding='utf-8') as f:
                r_json = f.read()
                l_attr = cls.from_json_string(r_json)
            l_inst = [cls.create(i) for i in l_attr]
            return l_inst
        else:
            with open("Square.json", encoding='utf-8') as f:
                r_json = f.read()
                l_attr = cls.from_json_string(r_json)
            l_inst = [cls.create(i) for i in l_attr]
            return l_inst
