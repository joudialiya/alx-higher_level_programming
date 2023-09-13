#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if a_dictionary:
        for key, i_value in a_dictionary.copy().items():
            if i_value == value:
                a_dictionary.pop(key)
    return (a_dictionary)
