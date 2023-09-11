#!/usr/bin/python3
# 11-delete_at.py


def delete_at(my_list=[], idx=0):
    leng = len(my_list)
    if idx >= 0 and idx < leng:
        del my_list[idx]
    return (my_list)
