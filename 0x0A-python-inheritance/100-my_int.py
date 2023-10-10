#!/usr/bin/python3
"""Rebel Int class module"""


class MyInt(int):
    """Rebel class"""
    def __eq__(self, other):
        """Overload == operator"""
        return super().__ne__(other)

    def __ne__(self, other):
        """Overload != operator"""
        return super().__eq__(other)
