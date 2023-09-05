#!/usr/bin/python3
for a in range(0, 10):
    for b in range(a + 1, 10):
        print("{:d}".format(a), end="")
        if a < 8:
            print("{:d}".format(b), end=", ")
        else:
            print("{:d}".format(b))
