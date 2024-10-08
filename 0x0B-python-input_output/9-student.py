#!/usr/bin/python3
"""Lerning about __dict__ and json"""


class Student:
    """Simple Student Class"""
    def __init__(self, first_name, last_name, age):
        """Constructor"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """To string"""
        return self.__dict__
