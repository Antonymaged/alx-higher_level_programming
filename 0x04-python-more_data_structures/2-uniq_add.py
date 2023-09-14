#!/usr/bin/python3


def uniq_add(my_list=[]):
    new_lis = sorted(my_list)
    leng = len(new_lis)
    sumy = 0
    for i in range(0, leng):
        sumy = sumy + new_lis[i]
    return (sumy)
