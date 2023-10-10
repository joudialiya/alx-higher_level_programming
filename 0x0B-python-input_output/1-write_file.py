#!/usr/bin/python3
"""Write exp Module"""


def write_file(filename="", text=""):
    """Write Function"""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
