#!/usr/bin/python3

def no_c(my_string):
    n = ""
    for c in my_string:
        if c != 'c' and c != 'C':
            n += c
    return (n)
