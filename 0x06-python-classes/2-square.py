#!/usr/bin/python3
""" Square (size)
arg : size - attr : _Square__size 
raise Error if size not int or less than 0"""


class Square:
    """ arg : size - attr : _Square__size 
        raise Error if size not int or less than 0"""
    n = 0
    def __init__(self, __size = 0):
        self._Square__size = __size
    try:
        n += self._Square__size
    except Exception:
        raise TypeError("size must be an integer")
    if self._Square__size < 0:
        raise ValueError("size must be >= 0")
