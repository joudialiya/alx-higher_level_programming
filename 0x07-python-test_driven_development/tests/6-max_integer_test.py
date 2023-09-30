#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest


max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """ unit test for max int """

    def test_empty(self):
        """ empty list """
        self.assertEqual(max_integer(), None)

    def test_simple(self):
        """ normal usage """
        self.assertEqual(max_integer([0, 2, 3, 4]), 4)

    def test_negetive(self):
        """ empty list """
        self.assertEqual(max_integer([0, -1, -2]), 0)

    def test_one_element(self):
        """ one element list """
        self.assertEqual(max_integer([0]), 0)

    def test_one_value(self):
        """ one value list """
        self.assertEqual(max_integer([0, 0, 0]), 0)
