#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    if not my_list:
        return
    cpy = my_list.copy()
    cpy.reverse()
    for i in cpy:
        print("{:d}".format(i))
