#!/usr/bin/python3
def best_score(a_dictionary):
    m = (None, None)
    if a_dictionary:
        for key, value in a_dictionary.items():
            if (not m[1]) or value > m[1]:
                m = (key, value)
    return (m[0])
