#!/usr/bin/python3
""" Module Doc"""


class Student:
    """ Class Doc"""

    def __init__(self, first_name, last_name, age):
        self.fname = first_name
        self.lname = last_name
        self.age = age

    def to_json(self):
        return {'first_name': self.fname,/
                'last_name': self.lname, 'age': self.age}
