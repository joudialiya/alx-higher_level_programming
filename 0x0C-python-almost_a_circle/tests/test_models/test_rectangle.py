#!/usr/bin/python3
""" Test Rectangle """


import unittest
from models.rectangle import Rectangle


class Test_rectangle(unittest.TestCase):
    """ Test Rectangle Class """

    def test_simple_rectangle_with_id(self):
        """ simplle rectangle """
        b = Rectangle(3, 2, 1, 5, 12)
        self.assertEqual(b.width, 3)
        self.assertEqual(b.height, 2)
        self.assertEqual(b.x, 1)
        self.assertEqual(b.y, 5)
        self.assertEqual(b.id, 12)

    def test_validate_width_type(self):
        """ Test the validation of the width """
        msg = "width must be an integer"
        self.assertRaisesRegex(TypeError, msg, Rectangle, 'a', 1)

    def test_validate_width_value(self):
        """ Test the validation of the width """
        msg = "width must be > 0"
        self.assertRaisesRegex(ValueError, msg, Rectangle, -1, 1)
        self.assertRaisesRegex(ValueError, msg, Rectangle, 0, 1)

    def test_validate_height_type(self):
        """ Test the validation of the height """
        msg = "height must be an integer"
        self.assertRaisesRegex(TypeError, msg, Rectangle, 1, 'a')

    def test_validate_height_value(self):
        """ Test the validation of the height """
        msg = "height must be > 0"
        self.assertRaisesRegex(ValueError, msg, Rectangle, 1, -1)
        self.assertRaisesRegex(ValueError, msg, Rectangle, 1, 0)

    def test_validate_x_type(self):
        """ Test the validation of the x """
        msg = "x must be an integer"
        self.assertRaisesRegex(TypeError, msg, Rectangle, 1, 1, 'a', 0)

    def test_validate_x_value(self):
        """ Test the validation of the x """
        msg = "x must be >= 0"
        self.assertRaisesRegex(ValueError, msg, Rectangle, 1, 1, -1, 1)

    def test_validate_y_type(self):
        """ Test the validation of the y """
        msg = "y must be an integer"
        self.assertRaisesRegex(TypeError, msg, Rectangle, 1, 1, 1, 'a')

    def test_validate_y_value(self):
        """ Test the validation of the y """
        msg = "y must be >= 0"
        self.assertRaisesRegex(ValueError, msg, Rectangle, 1, 1, 1, -1)

    def test_rectangle_str(self):
        """ rectangle string repr """
        b = Rectangle(2, 2, 2, 2, 12)
        self.assertEqual(str(b), "[Rectangle] (12) 2/2 - 2/2")

    def test_update_1_arg(self):
        """ update with 1 arg """
        b = Rectangle(1, 1, 2, 3)
        b.update(9)
        self.assertEqual(b.id, 9)

    def test_update_2_arg(self):
        """ update with 2 arg """
        b = Rectangle(1, 1, 2, 3)
        b.update(9, 9)
        self.assertEqual(b.id, 9)
        self.assertEqual(b.width, 9)

    def test_update_3_arg(self):
        """ update with 3 arg """
        b = Rectangle(1, 1, 2, 3)
        b.update(9, 9, 9)
        self.assertEqual(b.id, 9)
        self.assertEqual(b.width, 9)
        self.assertEqual(b.height, 9)

    def test_update_4_arg(self):
        """ update with 4 arg """
        b = Rectangle(1, 1, 2, 3)
        b.update(9, 9, 9, 9)
        self.assertEqual(b.id, 9)
        self.assertEqual(b.width, 9)
        self.assertEqual(b.height, 9)
        self.assertEqual(b.x, 9)

    def test_update_5_arg(self):
        """ update with 5 arg """
        b = Rectangle(1, 1, 2, 3)
        b.update(9, 9, 9, 9, 9)
        self.assertEqual(b.id, 9)
        self.assertEqual(b.width, 9)
        self.assertEqual(b.height, 9)
        self.assertEqual(b.x, 9)
        self.assertEqual(b.y, 9)

    def test_update_args_kwarg_priority(self):
        """ update with kwargs """
        b = Rectangle(1, 2, 3, 4)
        b.update(5, 5, y=9)
        self.assertEqual(b.width, 5)
        self.assertEqual(b.y, 4)

    def test_update_one_kwarg(self):
        """ update with kwargs """
        b = Rectangle(1, 2, 3, 4)
        b.update(height=9)
        self.assertEqual(b.height, 9)

    def test_update_three_kwarg(self):
        """ update with kwargs """
        b = Rectangle(1, 2, 3, 4)
        b.update(height=9, y=9, x=9, id=9, width=9)
        self.assertEqual(b.height, 9)
        self.assertEqual(b.y, 9)
        self.assertEqual(b.x, 9)
        self.assertEqual(b.id, 9)
        self.assertEqual(b.width, 9)

    def test_to_dictionary(self):
        """ test the function() """
        b = Rectangle(1, 2, 3, 4)
        dictionary = b.to_dictionary()
        self.assertIn("id", dictionary)
        self.assertIn("width", dictionary)
        self.assertIn("height", dictionary)
        self.assertIn("x", dictionary)
        self.assertIn("y", dictionary)
