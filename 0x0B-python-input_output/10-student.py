#!/usr/bin/python3
"""Lerning about __dict__ and json"""


class Student:
    """Simple Student Class"""
    def __init__(self, first_name, last_name, age):
        """Constructor"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """To string"""
        if type(attrs) is list:
            for element in attrs:
                if type(element) is not str:
                    return self.__dict__
            return dict(filter(lambda e: e[0] in attrs, self.__dict__.items()))
        return self.__dict__
