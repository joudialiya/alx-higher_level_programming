#!/usr/bin/python3
def uppercase(str):
    for i in range(0, len(str)):
        if ord(str[i]) >= ord('a') and ord(str[i]) <= ord('z'):
            out = ord('A') + ord('a') - ord(str[i])
        else:
            out = str[i]
        if (i == len(str) - 1):
            print("{:c}".format(out))
        else:
            print("{:c}".format(out), end="")
