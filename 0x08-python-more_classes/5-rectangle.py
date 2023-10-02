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
        return self.__height

    def set_height(self, val):
        """height setter"""
        if not isinstance(val, int):
            raise TypeError("height must be an integer")
        if val < 0:
            raise ValueError("height must be >= 0")
        self.__height = val

    height = property(get_height, set_height)

    def area(self):
        """calculate the area"""
        return (self.__width * self.__height)

    def perimeter(self):
        """calculate the perimeter"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return (2 * (self.__width + self.__height))

    def __str__(self):
        """print rectangle"""
        s = ""
        if self.__width == 0 or self.__height == 0:
            return ("")
        for line in range(0, self.__height):
            for column in range(0, self.__width):
                s += "#"
            s += "\n"
        s = s[:-1]
        return (s)

    def __repr__(self):
        """official repr"""
        return ("Rectangle({:d}, {:d})".format(self.__width, self.__height))

    def __del__(self):
        """Destuctor"""
        print("Bye rectangle...")

    def __init__(self, width=0, height=0):
        self.set_height(height)
        self.set_width(width)
