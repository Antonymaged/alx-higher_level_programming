#!/usr/bin/python3


def max_integer(my_list=[]):
    leng = len(my_list)
    if leng == 0:
        return (None)
    b = my_list[0]
    for i in range(leng):
        if my_list[i] > b:
            b = my_list[i]
    return (b)
