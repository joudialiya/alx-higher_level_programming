#!/usr/bin/python3
"""Rectangle Module"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


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
