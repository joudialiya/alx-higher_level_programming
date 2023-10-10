#!/usr/bin/python3
"""Rebel Int class module"""


class MyInt(int):
    def __eq__(self, other):
        return super().__ne__(other);

    def __ne__(self, other):
        return super().__eq__(other);
