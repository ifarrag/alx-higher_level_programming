#!/usr/bin/python3
""" Square is special Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Class Doc"""
    def __init__(self, size, x=0, y=0, id=None):
        self.__ss = size
        super().__init__(self.__ss, self.__ss, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ Update(id,size,x,y)"""
        if len(args) != 0:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[i]
                if i == 1:
                    self.size = args[i]
                if i == 2:
                    self.x = args[i]
                if i == 3:
                    self.y = args[i]
        elif len(kwargs) != 0:
            for y in kwargs:
                if y == "id":
                    self.id = kwargs[y]
                if y == "size":
                    self.size = kwargs[y]
                if y == "x":
                    self.x = kwargs[y]
                if y == "y":
                    self.y = kwargs[y]

    def to_dictionary(self):
        """Dictionary"""
        return dict({"id": self.id, "size": self.size,
                    "x": self.x, "y": self.y})

    def __str__(self):
        return "[Square] (" + str(self.id) + ") "\
                + str(self.x) + "/" + str(self.y)\
                + " - " + str(self.width)
