#!/usr/bin/python3
def uppercase(str):
    for c in str:
        if ord(c) >= ord('a') and ord(c) <= ord('z'):
            out = chr(ord("A") + ord(c) - ord("a"))
        else:
            out = c
        print("{:s}".format(out), end="")
    print("")
