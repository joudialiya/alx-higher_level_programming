#!/usr/bin/python3
""" Geometry module """


class BaseGeometry:
    """ Base class """
    def area(self):
        """calculate area"""
        raise Exception("area() is not implemented")
