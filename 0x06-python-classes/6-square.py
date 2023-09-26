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

    def __get_position(self):
        """Position getter"""
        return (self.__position)

    def __set_position(self, value):
        """Position setter"""
        if (type(value) is tuple and type(value[0]) is int
                and type(value[1]) is int and value[0] >= 0 and value[1] >= 0):
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    position = property(__get_position, __set_position)

    def __init__(self, size=0, position=(0, 0)):
        """
        the Square class constuctor
        """
        self.__set_size(size)
        self.__set_position(position)

    def area(self):
        """
        Calculate the area of the square based on size
        """
        return (self.__size ** 2)

    def my_print(self):
        """
        Print the square to the screen
        """
        for bs in range(0, self.position[1]):
            print()
        for i in range(0, self.size):
            for rs in range(0, self.position[0]):
                print(" ", end="")
            for j in range(0, self.size):
                print("#", end="")
            print()
