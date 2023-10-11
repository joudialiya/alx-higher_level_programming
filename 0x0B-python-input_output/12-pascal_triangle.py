#!/usr/bin/python3
"""Pascal triangle"""


def pascal_triangle(n):
    """The function"""
    array = []
    for line in range(0, n):
        row = []
        for i in range(0, line + 1):
            if i > 0 and i < line:
                row.append(array[line - 1][i - 1] + array[line - 1][i])
            else:
                row.append(1)
        array.append(row)
    return (array)
