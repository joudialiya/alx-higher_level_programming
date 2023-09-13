#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return (list(map(lambda column: list(map(lambda v: v*v, column)), matrix)))
