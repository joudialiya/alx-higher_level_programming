#!/usr/bin/python3
for a in range(0, 10):
    for b in range(a + 1, 10):
        print("%d" % (a), end="")
        if a < 8:
            print("%d" % (b), end=", ")
        else:
            print("%d" % (b))
