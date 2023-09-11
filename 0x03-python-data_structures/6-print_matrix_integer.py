#!/usr/bin/python3

def print_matrix_integers(matrix=[[]]):
    for column in matrix:
        for i in range(0, len(column), 1):
            print("{:d}".format(column[i]), end="")
            if (i + 1) != len(column):
                print(" ", end="")
        print()
