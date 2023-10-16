#!/usr/bin/python3
""" Base class test """


import unittest
import models.base


class Test_base(unittest.TestCase):
    """ Test Case for Base Class """
    def test_with_id(self):
        """ Twst with id """
        b = models.base.Base(2)
        self.assertEqual(b.id, 2)

    def test_with_id_set_to_none(self):
        """ Twst without id """
        b = models.base.Base()
        self.assertEqual(b.id, 1)
