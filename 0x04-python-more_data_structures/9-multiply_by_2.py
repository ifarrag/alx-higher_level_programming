#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_d = {}
    for i, x in a_dictionary.items():
        new_d[i] = x * 2
    return new_d
