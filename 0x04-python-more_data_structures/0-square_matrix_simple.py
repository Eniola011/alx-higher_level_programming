#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrx = []
    for idx in matrix:
        matrx.append(list(map(lambda x: x ** 2, idx)))
    return matrx
