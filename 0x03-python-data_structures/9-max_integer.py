#!/usr/bin/python3

def max_integer(my_list=[]):
    m = None
    for i in my_list:
        if (not m) or i > m:
            m = i
    return (m)
