#!/usr/bin/python3
""" prints the list, but sorted"""


class MyList(list):
"""    make list """
    def print_sorted(self):
        """ print sorted"""
        self.sor = list.sort()
        print(self.sor)
