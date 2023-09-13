#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    res = []
    res.extend(filter(lambda e: e not in set_1, set_2))
    res.extend(filter(lambda e: e not in set_2, set_1))
    return (set(res))
