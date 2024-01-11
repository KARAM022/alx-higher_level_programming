#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    nmatrix = matrix.copy()

    for i in range(len(matrix)):
        nmatrix[i] = list(map(lambda x: x**2, matrix[i]))

    return (nmatrix)
