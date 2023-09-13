#!/usr/bin/python3
def weight_average(my_list=[]):
    avg_sum = 0
    value = 0
    for score, weigth in my_list:
        avg_sum += weigth
        value += score * weigth
    if avg_sum == 0:
        return (0)
    else:
        return (value / avg_sum)
