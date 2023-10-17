#!/usr/bin/python3
""" Base class module """


import json
from io import StringIO


class Base:
    """ Base classs """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Class Constructor """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """ to json string """
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """ json => string """
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """ save to a file """
        with open(cls.__name__ + ".json", 'w') as file:
            if list_objs is None:
                d = []
            else:
                d = list(map(lambda e: e.to_dictionary(), list_objs))
            file.write(Base.to_json_string(d))

    @classmethod
    def create(cls, **dictionary):
        """ Factory Constructor """
        if cls.__name__ is "Rectangle":
            dummy = cls(1, 1)
        else:
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """ load instances from a json file """
        try:
            with open(cls.__name__ + ".json", "r") as file:
                json_string = file.read()
                d = Base.from_json_string(json_string)
                return list(map(lambda e: cls.create(**e), d))
        except FileNotFoundError:
            return []
