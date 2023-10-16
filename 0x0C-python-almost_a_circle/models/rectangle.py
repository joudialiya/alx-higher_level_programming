#!/usr/bin/python3
""" Rectangle Module """


from models.base import Base


class Rectangle(Base):
    """ Rectangle class """

    def __get_width(self):
        """width getter"""
        return self.__width

    def __set_width(self, width):
        """width setter"""
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    width = property(__get_width, __set_width)

    def __get_height(self):
        """height getter"""
        return self.__height

    def __set_height(self, height):
        """height setter"""
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    height = property(__get_height, __set_height)

    def __get_x(self):
        """x getter"""
        return self.__x

    def __set_x(self, x):
        """x setter"""
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    x = property(__get_x, __set_x)

    def __get_y(self):
        """y getter"""
        return self.__y

    def __set_y(self, y):
        """y setter"""
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    y = property(__get_y, __set_y)

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Rectangle Constructor """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    def area(self):
        """ Calculate the area """
        return (self.width * self.height)

    def display(self):
        """ print the rectagle """
        for row in range(0, self.y + self.height):
            if row >= self.y:
                for column in range(0, self.x + self.width):
                    if column < self.x:
                        print(" ", end="")
                    else:
                        print("#", end="")
            print()

    def __str__(self):
        """String repr"""
        args = (self.id, self.x, self.y, self.width, self.height)
        return "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format(*args)

    def update(self, *args, **kwargs):
        """ update using a pack of args """
        length = len(args)

        if length != 0:
            if length > 0:
                self.id = args[0]
            if length > 1:
                self.width = args[1]
            if length > 2:
                self.height = args[2]
            if length > 3:
                self.x = args[3]
            if length > 4:
                self.y = args[4]
        else:
            for (key, value) in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ return a dictionary that represent the object """
        dictionary = {}
        dictionary["y"] = self.y
        dictionary["x"] = self.x
        dictionary["id"] = self.id
        dictionary["width"] = self.width
        dictionary["height"] = self.height
        return dictionary
