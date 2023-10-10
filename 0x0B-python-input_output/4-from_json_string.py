#!/usr/bin/python3
"""Json Module"""
import json
from io import StringIO


def from_json_string(my_str):
    """Serialize Object"""
    return (json.load(StringIO(my_str)))
