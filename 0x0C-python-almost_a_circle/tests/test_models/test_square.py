#!/usr/bin/python3
""" Square Test Module """


import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """ Test Class """
    def test_constructor(self):
        """ normal use """
        size = 2
        b = Square(size)
        self.assertEqual(b.width, size)
        self.assertEqual(b.height, size)

    def test_square_str(self):
        """ test square str """
        size = 3
        b = Square(size, 2, 2, 12)
        self.assertEqual(str(b), "[Square] (12) 2/2 - 3")

    def test_size_property_normal(self):
        """ test seze proprty normal """
        b = Square(2, 2, 2)
        b.size = 3
        self.assertEqual(b.width, b.size)
        self.assertEqual(b.width, 3)

    def test_size_property_type_error(self):
        """ size property type error """
        b = Square(2, 2, 2)
        msg = "width must be an integer"
        self.assertRaisesRegex(TypeError, msg, setattr, b, "size", 'a')

    def test_size_property_value_error(self):
        """ size property type error """
        b = Square(2, 2, 2)
        msg = "width must be > 0"
        self.assertRaisesRegex(ValueError, msg, setattr, b, "size", 0)
