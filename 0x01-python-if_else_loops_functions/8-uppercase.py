#!/usr/bin/python3
def uppercase(str):
    for i in range(0, len(str)):
        if ord(str[i]) >= ord('a') and ord(str[i]) <= ord('z'):
            out = chr(ord("A") + ord(str[i]) - ord("a"))
        else:
            out = str[i]
        if (i == len(str) - 1):
            print("{:s}".format(out))
        else:
            print("{:s}".format(out), end="")
