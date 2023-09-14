#!/usr/bin/python3


def uniq_add(my_list=[]):
    new = sorted(set(my_list))
    sumy = 0
    for i in new:
        sumy = sumy + i
    return (sumy)
