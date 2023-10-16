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
