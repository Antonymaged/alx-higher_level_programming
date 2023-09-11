#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    lengx = len(matrix[])
    lengy = len(matrix[[]])
    for i in range(lengx):
        for j in range(lengy):
            print("{:d}".format(matrix[lengx][lengy]))
        print()
