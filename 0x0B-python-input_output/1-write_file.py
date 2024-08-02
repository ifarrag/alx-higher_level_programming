#!/usr/bin/python3
""" Doc"""


def write_file(filename="", text=""):
    """ Function Doc"""
    with open(filename, 'w', encoding="utf-8") as f:
        sumChars = f.write(text)
        return sumChars
