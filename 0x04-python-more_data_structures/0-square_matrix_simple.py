#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for i in matrix:
        item = list(map(lambda x: x*x, i))
        new_matrix.append(item)
    return new_matrix
