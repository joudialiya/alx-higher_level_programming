#!/usr/bin/python3
"""Magic Class Module"""


class MagicClass:
    """Magic Class"""
    def __init__(self, radius=0):
        """Constructor"""
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
                raise TypeError("radius must be a number")
        else:
            self.__radius = radius

    def area(self):
        """Return the area"""
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """Return the circumference"""
        return (2 * math.pi * self.__radius)
