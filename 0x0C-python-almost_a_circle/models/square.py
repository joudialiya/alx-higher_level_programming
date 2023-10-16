#!/usr/bin/python3
""" Square module """


from models.rectangle import Rectangle


class Square(Rectangle):
    """ Square Class """

    def __get_size(self):
        """ size getter """
        return self.width

    def __set_size(self, size):
        """ size setter """
        self.width = size
        self.height = size

    size = property(__get_size, __set_size)

    def __init__(self, size, x=0, y=0, id=None):
        """ Square Constructor """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ String repr """
        args = (self.id, self.x, self.y, self.width)
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(*args)

    def update(self, *args, **kwargs):
        """ update a square """
        length = len(args)
        if length != 0:
            if length > 0:
                self.id = args[0]
            if length > 1:
                self.size = args[1]
            if length > 2:
                self.x = args[2]
            if length > 3:
                self.y = args[3]
        else:
            for (key, value) in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ return a dictionary that represent the object """
        dictionary = {}
        dictionary["id"] = self.id
        dictionary["size"] = self.size
        dictionary["x"] = self.x
        dictionary["y"] = self.y
        return dictionary
