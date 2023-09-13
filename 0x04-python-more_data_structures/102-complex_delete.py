#!/usr/bin/python3
def complex_delete(a_dictionary, value):
   cpy = a_dictionary.copy();
   for key, i_value in a_dictionary.items():
       if i_value == value:
           cpy.pop(key);
    return (cpy)
