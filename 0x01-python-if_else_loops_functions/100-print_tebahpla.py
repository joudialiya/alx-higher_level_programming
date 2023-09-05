#!/usr/bin/python3
for i in range(25, -1, -1):
    if (i % 2 == 1):
        print("{:c}".format(ord('a') + i), end="")
    else:
        print("{:c}".format(ord('A') + i), end="")
