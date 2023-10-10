#!/usr/bin/python3
"""Write exp Module"""


def append_write(filename="", text=""):
    """Append Function"""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
