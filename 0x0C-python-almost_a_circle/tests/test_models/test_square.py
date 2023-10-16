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

    def test_update_1_arg(self):
        """ test update with 1 arg """
        b = Square(2, 2, 2)
        b.update(12)
        self.assertEqual(b.id, 12)

    def test_update_2_arg(self):
        """ test update with 2 arg """
        b = Square(2, 2, 2)
        b.update(12, 4)
        self.assertEqual(b.id, 12)
        self.assertEqual(b.size, 4)

    def test_update_3_arg(self):
        """ test update with 3 arg """
        b = Square(2, 2, 2)
        b.update(12, 4, 4)
        self.assertEqual(b.id, 12)
        self.assertEqual(b.size, 4)
        self.assertEqual(b.x, 4)

    def test_update_4_arg(self):
        """ test update with 4 arg """
        b = Square(2, 2, 2)
        b.update(12, 4, 4, 4)
        self.assertEqual(b.id, 12)
        self.assertEqual(b.size, 4)
        self.assertEqual(b.x, 4)
        self.assertEqual(b.y, 4)

    def test_update_args_kwargs_priority(self):
        """ test priority """
        b = Square(2, 2, 2)
        b.update(12, size=4)
        self.assertEqual(b.id, 12)
        self.assertEqual(b.size, 2)

    def test_update_kwargs(self):
        """ test priority """
        b = Square(2, 2, 2)
        b.update(x=4, size=4, y=4)
        self.assertEqual(b.x, 4)
        self.assertEqual(b.size, 4)
        self.assertEqual(b.y, 4)

    def test_to_dictionary(self):
        """ test the function() """
        b = Square(1, 2, 3)
        dictionary = b.to_dictionary()
        self.assertIn("id", dictionary)
        self.assertIn("size", dictionary)
        self.assertIn("x", dictionary)
        self.assertIn("y", dictionary)
