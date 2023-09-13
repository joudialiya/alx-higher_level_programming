#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    cpy = a_dictionary.copy()
    for key, value in cpy.items():
        cpy.update({key: value * 2})
    return (cpy)
