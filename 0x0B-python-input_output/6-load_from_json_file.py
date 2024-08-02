#!/usr/bin/python3
""" Module Doc"""


def load_from_json_file(filename):
    """ Function Doc"""
    import json
    with open(filename, encoding="utf-8") as f:
        return json.load(fp=f)
