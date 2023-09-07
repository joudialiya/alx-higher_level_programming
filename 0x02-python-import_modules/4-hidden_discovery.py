#!/usr/bin/python3
import hidden_4
dirs = dir(hidden_4)
for name in dirs:
    if name[0:2] != "__":
        print(name)
