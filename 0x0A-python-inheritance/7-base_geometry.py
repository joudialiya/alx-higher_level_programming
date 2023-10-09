#!/usr/bin/python3
""" Geometry module """


class BaseGeometry:
    """ Base class """
    def area(self):
        """calculate area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """int validator"""
        if (not isinstance(value, int)):
            raise TypeError("{:s} must be an integer".format(name))
        if (value < 0):
            raise ValueError("{:s} must be greater than 0".format(name))
