#!/usr/bin/python3
def common_elements(set_1, set_2):
    res = []
    for e in set_1:
        if e in set_2:
            res.append(e)
    return (res)
