#!/usr/bin/python3
""" Doc"""


def append_write(filename="", text=""):
    """ Function Doc"""
    with open(filename, 'a', encoding="utf-8") as f:
        sumChars = f.write(text)
        return sumChars
