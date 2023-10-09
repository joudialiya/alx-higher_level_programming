#!/usr/bin/python3
"""isClass module"""


def inherits_from(obj, a_class):
    """ is same class """
    return (issubclass(type(obj), a_class))
