#!/bin/usr/python3
""" Lookup function module """


def lookup(obj):
    """
    lookup function
        returns the list of available attributes and methods of an objec
    """
    return (obj.__dict__)
