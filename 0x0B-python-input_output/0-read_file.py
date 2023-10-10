#!/usr/bin/python3
"""Open file module"""


def read_file(filename=""):
    """Read a file"""
    with open(filename, "r", encoding="utf-8") as f:
        read_data = f.read()
        print(read_data, end="")
