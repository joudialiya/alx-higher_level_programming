#!/usr/bin/python3
from sys import argv


def main():
    print("{:d} ".format(len(argv) - 1), end="")
    if len(argv) - 1 == 1:
        print("argument", end="")
    else:
        print("arguments", end="")
    if len(argv) - 1 > 0:
        print(":")
        for i in range(1, len(argv)):
            print("{:d}: {:s}".format(i, argv[i]))
    else:
        print(".")


if __name__ == "__main__":
    main()
