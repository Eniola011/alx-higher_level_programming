#!/usr/bin/python3
"""
Matrix_divide Module:
Division of Elements in a matrix
"""


def matrix_divided(matrix, div):
    """Function divides all elements of a matrix.
    Args:
        matrix: list of lists of integers or floats
        div: int/float number to divide matrix
    Return:
        A new matrix
    Error:
        TypeError: If 'matrix' isn't int/float
                   If 'div' isn't int/float
                   If 'elem' in row in matrix aren't thesame size
                   If 'elem' in list aren't int/float
        ZeroDivisionError: If 'div' is equal to zero
    """
    error1 = "matrix must be a matrix (list of lists) of integers/floats"
    if not matrix or not isinstance(matrix, list):
        raise TypeError(error1)

    error2 = "Each row of the matrix must have the same size"
    element = 0
    for row in matrix:
        if not row or not isinstance(row, list):
            raise TypeError(error1)
        if element != 0 and len(row) != element:
            raise TypeError(error2)
        for value in row:
            if not isinstance(value, (int, float)):
                raise TypeError(error1)

        element = len(row)

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = [[round(elem / div, 2) for elem in row] for row in matrix]

    return new_matrix
