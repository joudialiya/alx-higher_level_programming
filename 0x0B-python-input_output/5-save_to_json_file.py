#!/usr/bin/python3
"""Selialize an object"""
import json


def save_to_json_file(my_obj, filename):
    """Selialize an object into a file"""
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
