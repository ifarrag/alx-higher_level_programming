#!/usr/bin/python3
""" prints the list, but sorted"""


class MyList(list):
    """ make list """
    def __init__(self):
        """init"""
        super().__init__()
        self.listit = list(MyList())

    def print_sorted(self):
        """ print sorted"""
        print(self.listit)
