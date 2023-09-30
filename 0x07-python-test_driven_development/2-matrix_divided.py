#!/usr/bin/python3
"""Simple math module"""


import math


def matrix_divided(matrix, div):
    """matrix devided"""
    msg = "matrix must be a matrix (list of lists) of integers/floats"
    if type(matrix) != list:
        raise TypeError(msg)
    for vector in matrix:
        if type(vector) != list:
            raise TypeError(msg)
        if len(vector) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for e in vector:
            if type(e) != int and type(e) != float:
                raise TypeError(msg)

    if type(div) != int and type(div) != float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    m = matrix
    return list(map(lambda v: list(map(lambda e: round(e / div, 2), v)), m))
