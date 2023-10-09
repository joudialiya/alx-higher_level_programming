#!/usr/bin/python3
"""isClass module"""


def is_kind_of_class(obj, a_class):
    """ is same class """
    return (isinstance(obj, a_class) or issubclass(type(obj), a_class))
