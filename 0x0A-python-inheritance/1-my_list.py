#!/usr/bin/python3
""" prints the list, but sorted"""


class MyList(list):
    """ make list """
    New = MyList()
    def __init__(self):
        """init"""
        super().__init__()
        self.temp = MyList() + New

    def print_sorted(self):
        """ print sorted"""
        self.temp.sort()
        print(self.temp)
