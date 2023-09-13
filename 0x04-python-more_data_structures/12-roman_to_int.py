#!/usr/bin/python3
def roman_to_int(string):
    number = 0
    symbols = [
        ("M", 1000),
        ("D", 500),
        ("C", 100),
        ("L", 50),
        ("X", 10),
        ("V", 5),
        ("I", 1)
    ]
    i_string = 0
    i_symbol = 0
    while i_string < len(string):
        before_count = 0
        after_count = 0
        middle_stone = False
        late_stone = False

        for c in string[i_string:]:
            if string[i_string] == symbols[i_symbol][0]:
                i_string += 1
                before_count += 1
            else:
                break
        if i_symbol > 0 and i_string < len(string):
            if string[i_string] == symbols[i_symbol - 1][0]:
                middle_stone = True
                i_string += 1
        for c in string[i_string:]:
            if string[i_string] == symbols[i_symbol][0]:
                i_string += 1
                after_count += 1
            else:
                break
        if i_symbol > 1 and i_string < len(string):
            if string[i_string] == symbols[i_symbol - 2][0]:
                late_stone = True
                i_string += 1

        if before_count == 0 and after_count == 0 and middle_stone is False:
            i_symbol += 2
            continue
        else:
            pass
        if late_stone:
            number += symbols[i_symbol - 2][1]
            number -= symbols[i_symbol][1] * before_count
        elif middle_stone:
            number += symbols[i_symbol - 1][1]
            number += symbols[i_symbol][1] * (after_count - before_count)
        else:
            number += symbols[i_symbol][1] * before_count
    return (number)
