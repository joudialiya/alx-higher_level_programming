#!/usr/bin/python3
def magic_string():
    return (", ".join(["BestSchool"]  * (magic_string.n := magic_string.n + 1)))
magic_string.n = 0
