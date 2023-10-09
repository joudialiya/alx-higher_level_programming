#!/usr/bin/python3
""" Lookup function module """


def lookup(obj):
    """
    lookup function
        returns the list of available attributes and methods of an objec
    """
    return (list(obj.__dict__))
