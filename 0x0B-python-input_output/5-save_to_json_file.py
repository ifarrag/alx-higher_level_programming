#!/usr/bin/python3
""" Module Doc"""


def save_to_json_file(my_obj, filename):
    """ Function Doc"""
    import json
    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(my_obj, fp=f.write())
