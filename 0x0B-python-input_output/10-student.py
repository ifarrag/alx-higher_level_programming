#!/usr/bin/python3
""" Module Doc"""


class Student:
    """ Class Doc"""

    def __init__(self, first_name, last_name, age):
        self.fname = first_name
        self.lname = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ Method Doc"""

        if type(attrs) is list and attrs is not None:
            new_dict = dict()
            for i in attrs:
                if i == 'first_name':
                    new_dict('first_name') = self.fname
                if i == 'last_name':
                    new_dict('last_name') = self.lname
                if i == 'age':
                    new_dict('age') = self.age
            return new_dict

        else:
            return {'first_name': self.fname,
                    'last_name': self.lname, 'age': self.age}
