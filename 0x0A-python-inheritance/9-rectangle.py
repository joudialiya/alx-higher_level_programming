#!/usr/bin/python3
"""Rectangle Module"""


class BaseGeometry:
    """ Base class """
    def area(self):
        """calculate area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """int validator"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """Rectangle class"""
    def __init__(self, width, height):
        """Class Constructor"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """calcualte area"""
        return (self.__height * self.__width)

    def __str__(self):
        """str repr"""
        return ("[Rectangle] {:d}/{:d}".format(self.__width, self.__height))
