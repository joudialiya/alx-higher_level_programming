#!/usr/bin/python3
"""Selialize an object"""
import json
from io import StringIO


def load_from_json_file(filename):
    """Selialize an object into a file"""
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(StringIO(f.read()))
