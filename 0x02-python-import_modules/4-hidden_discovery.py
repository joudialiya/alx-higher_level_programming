#!/usr/bin/python3
import hidden_4


def main():
    dirs = dir(hidden_4)
    for name in dirs:
        if name[0:2] != "__":
            print(name)


if __name__ == "__main__":
    main()
