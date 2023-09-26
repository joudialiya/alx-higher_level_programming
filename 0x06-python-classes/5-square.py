#!/usr/bin/python3
"""
The purpose of this module is to grasp OOP in python
"""


class Square:
    """
    Square Class
    """

    def __get_size(self):
        """
        size getter
        """
        return (self.__size)

    def __set_size(self, size):
        """
        size setter
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    size = property(__get_size, __set_size)

    def __init__(self, size=0):
        """
        the Square class constuctor
        """
        self.__set_size(size)

    def area(self):
        """
        Calculate the area of the square based on size
        """
        return (self.__size ** 2)

    def my_print(self):
        """
        Print the square to the screen
        """
        for i in range(0, self.size):
            for j in range(0, self.size):
                print("#", end="")
            print()
