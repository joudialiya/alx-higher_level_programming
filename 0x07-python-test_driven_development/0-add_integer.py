#!/usr/bin/python3
"""Simple math module"""

import math


def add_integer(a, b=98):
    """add two numbers"""
    if type(a) != int and type(a) != float:
        raise TypeError("a must be an integer")
    if type(b) != int and type(b) != float:
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
