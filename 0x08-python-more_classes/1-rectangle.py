#!/usr/bin/python3
"""Rectangle Module"""


class Rectangle:
    """Rectangle Class"""

    def get_width(self):
        """width getter"""
        return self.__width

    def set_width(self, val):
        """width setter"""
        if not isinstance(val, int):
            raise TypeError("width must be an integer")
        if val < 0:
            raise ValueError("width must be >= 0")
        self.__width = val

    width = property(get_width, set_width)

    def get_heigth(self):
        """height getter"""
        return self.__heigth

    def set_heigth(self, val):
        """heigth setter"""
        if not isinstance(val, int):
            raise TypeError("heigth must be an integer")
        if val < 0:
            raise ValueError("heigth must be >= 0")
        self.__heigth = val

    heigth = property(get_heigth, set_heigth)

    def __init__(self, width=0, heigth=0):
        self.set_heigth(heigth)
        self.set_width(width)
