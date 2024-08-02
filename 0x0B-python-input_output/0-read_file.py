#!/usr/bin/python3
""" read()"""


def read_file(filename=""):
    """ return read() """

    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
        return f.read()
