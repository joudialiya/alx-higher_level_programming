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

    def get_height(self):
        """height getter"""
        return self.__heigth

    def set_height(self, val):
        """height setter"""
        if not isinstance(val, int):
            raise TypeError("heigth must be an integer")
        if val < 0:
            raise ValueError("heigth must be >= 0")
        self.__height = val

    height = property(get_height, set_height)

    def __init__(self, width=0, height=0):
        self.set_height(height)
        self.set_width(width)
