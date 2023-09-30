#!/usr/bin/python3

""" Text Manipulation """


def text_indentation(text):
    """ text tokenizer """
    if type(text) != str:
        raise TypeError("text must be a string")

    res = text
    for delim in ['.', ':', '?']:
        res = (delim + "\n\n").join(
            list(map(lambda string: string.strip(" "), res.split(delim))))
    print(res, end="")
