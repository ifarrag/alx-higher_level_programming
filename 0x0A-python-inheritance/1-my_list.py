#!/usr/bin/python3
""" prints the list, but sorted"""


class MyList(list):
    """ make list """
    def __init__(self):
        """init"""
        super().__init__()

    def print_sorted(self):
        """ print sorted"""
        beSort = list.self
        beSort.sort()
        print(beSort)
