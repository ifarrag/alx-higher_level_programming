#!/usr/bin/python3
""" DOC """


class MyList(list):
"""    make list """
    def __init__(self):
        """  __init__ """
        super().__init__()

    def print_sorted(self):
        """ print sorted"""
        self.sor = list.sort()
        print(self.sor)
