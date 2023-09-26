#!/usr/bin/python3


class Square:
    """
    Square Class
    """
    def __init__(self, size=0):
        """
        the Square class constuctor
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
