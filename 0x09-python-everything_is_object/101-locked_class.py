#!/usr/bin/python3
"""Locked Class Module"""


class LockedClass:
    """Locked class"""
    def __setattr__(self, key, value):
        """custom __setasttr__"""
        if key != "first_name":
            msg = "'LockedClass' object has no attribute '{}'".format(key)
            raise AttributeError(msg)
        object.__setattr__(self, key, value)
