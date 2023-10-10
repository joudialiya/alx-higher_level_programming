#!/usr/bin/python3
""" add attrebute module """


def add_attribute(obj, attr, value):
    """Add new attrebute"""
    if "__dict__" not in dir(obj):
        raise TypeError("can't add new attribute")
    if attr in list(obj.__dict__):
        raise TypeError("can't add new attribute")
    if "__slots__" in list(obj.__dict__):
        raise TypeError("can't add new attribute")
    setattr(obj, attr, value)
