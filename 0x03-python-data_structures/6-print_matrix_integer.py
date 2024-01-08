#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix or not matrix[0]:
        print()
    for x in matrix:
        for i, j in enumerate(x):
            if i < len(x) - 1:
                print("{:d} ".format(j), end="")
            else:
                print("{:d}".format(j), end="")
        print()
