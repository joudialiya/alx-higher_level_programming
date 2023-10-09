#!/usr/bin/python3
""" A sorted list module """


class MyList(list):
    """A list that print element in a sorted manner"""
    def print_sorted(self):
        """Print a sorted list"""
        print(sorted(self))
