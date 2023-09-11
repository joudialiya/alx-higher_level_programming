#!/usr/bin/python3

def multiple_returns(sentense):
    first_char = None
    if len(sentense) > 0:
        first_char = sentense[0]
    return (first_char, len(sentense))
